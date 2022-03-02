from django import forms
from django.contrib import admin, messages
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from ordered_model.admin import (
    OrderedInlineModelAdminMixin,
    OrderedModelAdmin,
    OrderedTabularInline,
)

from domain_events.publisher import send_schedule_invitation_email
from users.autocomplete import UsersBackendAutocomplete

from .models import (
    Day,
    DayRoomThroughModel,
    Room,
    ScheduleItem,
    ScheduleItemAdditionalSpeaker,
    ScheduleItemInvitation,
    Slot,
)


@admin.action(description="Send schedule invitation to all (waiting confirmation)")
def send_schedule_invitation_to_all(modeladmin, request, queryset):
    # We only want to send it to those we are still waiting for confirmation
    # and that have a submission
    _send_invitations(queryset=queryset)
    messages.add_message(request, messages.INFO, "Invitations sent")


@admin.action(
    description="Send schedule invitation to uninvited (waiting confirmation)"
)
def send_schedule_invitation_to_uninvited(modeladmin, request, queryset):
    # We only want to send it to those we are still waiting for confirmation
    # and that have a submission
    _send_invitations(queryset=queryset, uninvited_only=True)
    messages.add_message(request, messages.INFO, "Invitations sent")


def _send_invitations(*, queryset, uninvited_only: bool = False):
    queryset = queryset.filter(
        status=ScheduleItem.STATUS.waiting_confirmation,
        submission__isnull=False,
        type__in=[
            ScheduleItem.TYPES.submission,
            ScheduleItem.TYPES.training,
        ],
    )

    if uninvited_only:
        queryset = queryset.filter(speaker_invitation_sent_at__isnull=True)

    for schedule_item in queryset:
        schedule_item.speaker_invitation_sent_at = timezone.now()
        send_schedule_invitation_email(schedule_item)
        schedule_item.save()


class SlotInline(admin.TabularInline):
    model = Slot


class ScheduleItemAdditionalSpeakerInlineForm(forms.ModelForm):
    class Meta:
        model = ScheduleItemAdditionalSpeaker
        widgets = {
            "user_id": UsersBackendAutocomplete(admin.site),
        }
        fields = ["scheduleitem", "user_id"]


class ScheduleItemAdditionalSpeakerInline(admin.TabularInline):
    model = ScheduleItemAdditionalSpeaker
    form = ScheduleItemAdditionalSpeakerInlineForm


@admin.register(ScheduleItem)
class ScheduleItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "conference",
        "status",
        "language",
        "slot",
        "type",
        "submission",
    )
    list_filter = ("conference", "status", "type")
    ordering = ("conference", "slot")
    fieldsets = (
        (
            _("Event"),
            {
                "fields": (
                    "conference",
                    "type",
                    "status",
                    "language",
                    "title",
                    "slug",
                    "image",
                    "highlight_color",
                    "audience_level",
                    "description",
                    "submission",
                )
            },
        ),
        (_("Schedule"), {"fields": ("slot", "duration", "rooms")}),
        (
            _("Invitation"),
            {"fields": ("speaker_invitation_notes", "speaker_invitation_sent_at")},
        ),
    )
    autocomplete_fields = ("submission",)
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("rooms",)
    inlines = [
        ScheduleItemAdditionalSpeakerInline,
    ]
    actions = [
        send_schedule_invitation_to_all,
        send_schedule_invitation_to_uninvited,
    ]


@admin.register(ScheduleItemInvitation)
class ScheduleItemInvitationAdmin(admin.ModelAdmin):
    list_display = (
        "slot",
        "status",
        "title",
        "conference",
        "speaker_invitation_notes",
        "speaker_invitation_sent_at",
        "open_schedule_item",
        "open_submission",
    )
    list_filter = (
        "conference",
        "slot",
        "status",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slot",
                    "status",
                    "speaker_invitation_notes",
                    "speaker_invitation_sent_at",
                    "conference",
                    "open_schedule_item",
                    "open_submission",
                ),
            },
        ),
    )

    def open_schedule_item(self, obj) -> str:
        url = reverse("admin:schedule_scheduleitem_change", args=[obj.id])
        return mark_safe(f'<a class="button" target="_blank" href="{url}">Schedule</a>')

    def open_submission(self, obj) -> str:
        url = reverse("admin:submissions_submission_change", args=[obj.id])
        return mark_safe(
            f'<a class="button" target="_blank" href="{url}">Submission</a>'
        )

    def has_add_permission(self, *args, **kwargs) -> bool:
        return False

    def has_delete_permission(self, *args, **kwargs) -> bool:
        return False

    def has_change_permission(self, *args, **kwargs) -> bool:
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(
            submission__isnull=False,
        ).order_by("slot__day", "slot__hour")


@admin.register(Room)
class RoomAdmin(OrderedModelAdmin):
    list_display = ("name", "conference")
    list_filter = ("conference",)


class DayRoomThroughModelInline(OrderedTabularInline):
    model = DayRoomThroughModel
    fields = (
        "room",
        "order",
        "move_up_down_links",
    )
    readonly_fields = (
        "order",
        "move_up_down_links",
    )


@admin.register(Day)
class DayAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    list_display = ("day", "conference")
    list_filter = ("conference",)
    inlines = (SlotInline, DayRoomThroughModelInline)
