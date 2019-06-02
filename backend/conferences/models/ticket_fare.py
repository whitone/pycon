from django.db import models
from django.utils import timezone

from django.utils.translation import ugettext_lazy as _

from model_utils.models import TimeFramedModel, TimeStampedModel


class TicketFare(TimeFramedModel, TimeStampedModel):
    conference = models.ForeignKey(
        'conferences.Conference',
        on_delete=models.CASCADE,
        verbose_name=_('conference'),
        related_name='ticket_fares'
    )

    code = models.CharField(_('code'), max_length=10)
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'))
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)

    @property
    def is_available(self):
        if not self.start or not self.end:
            return False

        now = timezone.now()
        return self.start <= now <= self.end

    def __str__(self):
        return f'{self.name} ({self.conference.name})'

    class Meta:
        verbose_name = _('Ticket Fare')
        verbose_name_plural = _('Ticket fares')
        unique_together = ('conference', 'code',)
