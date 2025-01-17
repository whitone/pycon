from datetime import datetime
from unittest.mock import patch

import pytest
import time_machine
from conferences.models.speaker_voucher import SpeakerVoucher
from schedule.models import ScheduleItem
import respx
from django.conf import settings
from django.utils import timezone
from pythonit_toolkit.emails.templates import EmailTemplate

from domain_events.handler import (
    handle_grant_reply_approved_sent,
    handle_grant_reply_rejected_sent,
    handle_grant_reply_waiting_list_sent,
    handle_new_cfp_submission,
    handle_new_schedule_invitation_answer,
    handle_schedule_invitation_sent,
    handle_speaker_communication_sent,
    handle_speaker_voucher_email_sent,
    handle_submission_time_slot_changed,
    handle_grant_voucher_email_sent,
)
from grants.models import Grant


pytestmark = pytest.mark.django_db


@pytest.mark.django_db
def test_handle_new_cfp_submission(conference_factory):
    conference = conference_factory(
        slack_new_proposal_comment_incoming_webhook_url="https://123",
        slack_new_proposal_incoming_webhook_url="https://456",
    )

    data = {
        "title": "test_title",
        "elevator_pitch": "test_elevator_pitch",
        "submission_type": "test_submission_type",
        "admin_url": "test_admin_url",
        "topic": "test_topic",
        "duration": "50",
        "speaker_id": 10,
        "conference_id": conference.id,
        "tags": "a,b",
    }

    with patch("domain_events.handler.slack") as slack_mock, respx.mock as req_mock:
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 10,
                            "fullname": "Marco Acierno",
                            "name": "Marco",
                            "username": "marco",
                        }
                    ]
                }
            }
        )
        handle_new_cfp_submission(data)

    slack_mock.send_message.assert_called_once()
    assert "Marco Acierno" in str(slack_mock.send_message.mock_calls[0])
    assert "https://456" in str(slack_mock.send_message.mock_calls[0])


def test_handle_schedule_invitation_sent():
    data = {
        "speaker_id": 10,
        "invitation_url": "https://url",
        "submission_title": "Title title",
    }

    with patch(
        "domain_events.handler.send_email"
    ) as email_mock, respx.mock as req_mock:
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 10,
                            "fullname": "Marco Acierno",
                            "name": "Marco",
                            "username": "marco",
                            "email": "marco@placeholder.it",
                        },
                    ]
                }
            }
        )

        handle_schedule_invitation_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.SUBMISSION_ACCEPTED,
        to="marco@placeholder.it",
        subject="[PyCon Italia 2023] Your submission was accepted!",
        variables={
            "submissionTitle": "Title title",
            "firstname": "Marco Acierno",
            "invitationlink": "https://url",
        },
    )


def test_handle_schedule_invitation_sent_reminder():
    data = {
        "speaker_id": 10,
        "invitation_url": "https://url",
        "submission_title": "Title title",
        "is_reminder": True,
    }

    with patch(
        "domain_events.handler.send_email"
    ) as email_mock, respx.mock as req_mock:
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 10,
                            "fullname": "Marco Acierno",
                            "name": "Marco",
                            "username": "marco",
                            "email": "marco@placeholder.it",
                        },
                    ]
                }
            }
        )

        handle_schedule_invitation_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.SUBMISSION_ACCEPTED,
        to="marco@placeholder.it",
        subject=(
            "[PyCon Italia 2023] Reminder: Your submission was "
            "accepted, confirm your presence"
        ),
        variables={
            "submissionTitle": "Title title",
            "firstname": "Marco Acierno",
            "invitationlink": "https://url",
        },
    )


def test_handle_submission_time_slot_changed():
    data = {
        "speaker_id": 10,
        "invitation_url": "https://url",
        "submission_title": "Title title",
    }

    with patch(
        "domain_events.handler.send_email"
    ) as email_mock, respx.mock as req_mock:
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 10,
                            "fullname": "Marco Acierno",
                            "name": "Marco",
                            "username": "marco",
                            "email": "marco@placeholder.it",
                        },
                    ]
                }
            }
        )

        handle_submission_time_slot_changed(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.SUBMISSION_SCHEDULE_TIME_CHANGED,
        to="marco@placeholder.it",
        subject="[PyCon Italia 2023] Your Submission time slot has been changed!",
        variables={
            "submissionTitle": "Title title",
            "firstname": "Marco Acierno",
            "invitationlink": "https://url",
        },
    )


def test_handle_new_schedule_invitation_answer(
    settings, schedule_item_factory, submission_factory
):
    settings.SPEAKERS_EMAIL_ADDRESS = "speakers@placeholder.com"
    schedule_item = schedule_item_factory(
        type=ScheduleItem.TYPES.talk, submission=submission_factory(speaker_id=10)
    )

    data = {
        "speaker_id": 10,
        "schedule_item_id": schedule_item.id,
        "speaker_notes": "Sub",
        "invitation_admin_url": "https://admin",
        "schedule_item_admin_url": "https://schedule",
    }

    with patch("domain_events.handler.slack") as slack_mock, respx.mock as req_mock:
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 10,
                            "fullname": "Marco Acierno",
                            "name": "Marco",
                            "username": "marco",
                            "email": "marco@placeholder.it",
                        },
                    ]
                }
            }
        )

        handle_new_schedule_invitation_answer(data)

    slack_mock.send_message.assert_called_once()


def test_handle_speaker_voucher_email_sent(settings, speaker_voucher_factory):
    settings.SPEAKERS_EMAIL_ADDRESS = "speakers@placeholder.com"
    speaker_voucher = speaker_voucher_factory(
        user_id=10,
        voucher_type=SpeakerVoucher.VoucherType.SPEAKER,
        voucher_code="ABC123",
    )

    data = {
        "speaker_voucher_id": speaker_voucher.id,
    }

    with patch(
        "domain_events.handler.send_email"
    ) as email_mock, respx.mock as req_mock:
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 10,
                            "fullname": "Marco Acierno",
                            "name": "Marco",
                            "username": "marco",
                            "email": "marco@placeholder.it",
                        },
                    ]
                }
            }
        )

        handle_speaker_voucher_email_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.SPEAKER_VOUCHER_CODE,
        to="marco@placeholder.it",
        subject="[PyCon Italia 2023] Your Speaker Voucher Code",
        variables={
            "firstname": "Marco Acierno",
            "voucherCode": "ABC123",
            "is_speaker_voucher": True,
        },
        reply_to=["speakers@placeholder.com"],
    )


def test_handle_speaker_voucher_email_sent_cospeaker(settings, speaker_voucher_factory):
    settings.SPEAKERS_EMAIL_ADDRESS = "speakers@placeholder.com"
    speaker_voucher = speaker_voucher_factory(
        user_id=10,
        voucher_type=SpeakerVoucher.VoucherType.CO_SPEAKER,
        voucher_code="ABC123",
    )

    data = {
        "speaker_voucher_id": speaker_voucher.id,
    }

    with patch(
        "domain_events.handler.send_email"
    ) as email_mock, respx.mock as req_mock, time_machine.travel(
        "2020-10-10 10:00:00Z", tick=False
    ):
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 10,
                            "fullname": "Marco Acierno",
                            "name": "Marco",
                            "username": "marco",
                            "email": "marco@placeholder.it",
                        },
                    ]
                }
            }
        )

        handle_speaker_voucher_email_sent(data)
        speaker_voucher.refresh_from_db()
        assert speaker_voucher.voucher_email_sent_at == datetime(
            2020, 10, 10, 10, 0, 0, tzinfo=timezone.utc
        )

    email_mock.assert_called_once_with(
        template=EmailTemplate.SPEAKER_VOUCHER_CODE,
        to="marco@placeholder.it",
        subject="[PyCon Italia 2023] Your Speaker Voucher Code",
        variables={
            "firstname": "Marco Acierno",
            "voucherCode": "ABC123",
            "is_speaker_voucher": False,
        },
        reply_to=["speakers@placeholder.com"],
    )


@pytest.mark.django_db
def test_handle_grant_approved_ticket_only_reply_sent(
    conference_factory, grant_factory, mock_users_by_ids, settings
):
    settings.FRONTEND_URL = "https://pycon.it"

    conference = conference_factory(
        start=datetime(2023, 5, 2, tzinfo=timezone.utc),
        end=datetime(2023, 5, 5, tzinfo=timezone.utc),
    )
    grant = grant_factory(
        conference=conference,
        approved_type=Grant.ApprovedType.ticket_only,
        applicant_reply_deadline=datetime(2023, 2, 1, 23, 59, tzinfo=timezone.utc),
        total_amount=680,
    )

    data = {
        "grant_id": grant.id,
        "is_reminder": False,
    }

    with patch("domain_events.handler.send_email") as email_mock:
        handle_grant_reply_approved_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.GRANT_APPROVED_TICKET_ONLY,
        to="marco@placeholder.it",
        subject=f"[{grant.conference.name}] Financial Aid Update",
        variables={
            "firstname": "Marco Acierno",
            "conferenceName": grant.conference.name.localize("en"),
            "startDate": "2 May",
            "endDate": "6 May",
            "deadlineDateTime": "1 February 2023 23:59 UTC",
            "deadlineDate": "1 February 2023",
            "replyLink": "https://pycon.it/grants/reply/",
        },
        reply_to=["grants@pycon.it"],
    )


@pytest.mark.django_db
def test_handle_grant_approved_ticket_travel_accommodation_reply_sent(
    conference_factory, grant_factory, mock_users_by_ids, settings
):
    settings.FRONTEND_URL = "https://pycon.it"

    conference = conference_factory(
        start=datetime(2023, 5, 2, tzinfo=timezone.utc),
        end=datetime(2023, 5, 5, tzinfo=timezone.utc),
    )
    grant = grant_factory(
        conference=conference,
        approved_type=Grant.ApprovedType.ticket_travel_accommodation,
        applicant_reply_deadline=datetime(2023, 2, 1, 23, 59, tzinfo=timezone.utc),
        travel_amount=680,
    )
    data = {
        "grant_id": grant.id,
        "is_reminder": False,
    }

    with patch("domain_events.handler.send_email") as email_mock:
        handle_grant_reply_approved_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.GRANT_APPROVED_TICKET_TRAVEL_ACCOMMODATION,
        to="marco@placeholder.it",
        subject=f"[{grant.conference.name}] Financial Aid Update",
        variables={
            "firstname": "Marco Acierno",
            "conferenceName": grant.conference.name.localize("en"),
            "startDate": "2 May",
            "endDate": "6 May",
            "amount": "680",
            "deadlineDateTime": "1 February 2023 23:59 UTC",
            "deadlineDate": "1 February 2023",
            "replyLink": "https://pycon.it/grants/reply/",
        },
        reply_to=["grants@pycon.it"],
    )


@pytest.mark.django_db
def test_handle_grant_reply_sent_reminder(
    conference_factory, grant_factory, mock_users_by_ids, settings
):
    settings.FRONTEND_URL = "https://pycon.it"
    conference = conference_factory(
        start=datetime(2023, 5, 2, tzinfo=timezone.utc),
        end=datetime(2023, 5, 5, tzinfo=timezone.utc),
    )
    grant = grant_factory(
        conference=conference,
        approved_type=Grant.ApprovedType.ticket_only,
        applicant_reply_deadline=datetime(2023, 2, 1, 23, 59, tzinfo=timezone.utc),
        total_amount=680,
    )
    data = {
        "grant_id": grant.id,
        "is_reminder": True,
    }

    with patch("domain_events.handler.send_email") as email_mock:
        handle_grant_reply_approved_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.GRANT_APPROVED_TICKET_ONLY,
        to="marco@placeholder.it",
        subject=f"[{grant.conference.name}] Reminder: Financial Aid Update",
        variables={
            "firstname": "Marco Acierno",
            "conferenceName": grant.conference.name.localize("en"),
            "startDate": "2 May",
            "endDate": "6 May",
            "deadlineDateTime": "1 February 2023 23:59 UTC",
            "deadlineDate": "1 February 2023",
            "replyLink": "https://pycon.it/grants/reply/",
        },
        reply_to=["grants@pycon.it"],
    )


@pytest.mark.django_db
def test_handle_grant_reply_waiting_list_sent(
    deadline_factory, conference, grant_factory, mock_users_by_ids, settings
):
    settings.FRONTEND_URL = "https://pycon.it"

    deadline_factory(
        start=datetime(2023, 3, 1, 23, 59, tzinfo=timezone.utc),
        conference=conference,
        type="custom",
        name={
            "en": "Update Grants in Waiting List",
            "it": "Update Grants in Waiting List",
        },
    )
    grant = grant_factory(conference=conference)

    data = {
        "grant_id": grant.id,
    }

    with patch("domain_events.handler.send_email") as email_mock:
        handle_grant_reply_waiting_list_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.GRANT_WAITING_LIST,
        to="marco@placeholder.it",
        subject=f"[{grant.conference.name}] Financial Aid Update",
        variables={
            "firstname": "Marco Acierno",
            "conferenceName": grant.conference.name.localize("en"),
            "replyLink": "https://pycon.it/grants/reply/",
            "grantsUpdateDeadline": "1 March 2023",
        },
        reply_to=["grants@pycon.it"],
    )


@pytest.mark.django_db
def test_handle_grant_reply_rejected_sent(grant, mock_users_by_ids):
    data = {
        "grant_id": grant.id,
    }

    with patch("domain_events.handler.send_email") as email_mock:
        handle_grant_reply_rejected_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.GRANT_REJECTED,
        to="marco@placeholder.it",
        subject=f"[{grant.conference.name}] Financial Aid Update",
        variables={
            "firstname": "Marco Acierno",
            "conferenceName": grant.conference.name.localize("en"),
        },
        reply_to=["grants@pycon.it"],
    )


def test_handle_grant_voucher_email_sent(settings, grant_factory):
    grant = grant_factory(
        user_id=10,
        voucher_code="ABC123",
    )

    data = {
        "grant_id": grant.id,
    }

    with patch(
        "domain_events.handler.send_email"
    ) as email_mock, respx.mock as req_mock:
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 10,
                            "fullname": "Marco Acierno",
                            "name": "Marco",
                            "username": "marco",
                            "email": "marco@placeholder.it",
                        },
                    ]
                }
            }
        )

        handle_grant_voucher_email_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.GRANT_VOUCHER_CODE,
        to="marco@placeholder.it",
        subject=f"[{grant.conference.name}] Your Grant Voucher Code",
        variables={
            "firstname": "Marco Acierno",
            "voucherCode": "ABC123",
        },
        reply_to=["grants@pycon.it"],
    )


@pytest.mark.parametrize("has_ticket", [True, False])
def test_handle_speaker_communication_sent_to_speakers_without_ticket(
    settings, requests_mock, conference_factory, has_ticket
):
    settings.SPEAKERS_EMAIL_ADDRESS = "reply"
    conference = conference_factory()
    data = {
        "user_id": 1,
        "subject": "test subject",
        "body": "test body",
        "only_speakers_without_ticket": True,
        "conference_id": conference.id,
    }
    requests_mock.post(
        f"{settings.PRETIX_API}organizers/{conference.pretix_organizer_id}/events/{conference.pretix_event_id}/tickets/attendee-has-ticket/",
        json={"user_has_admission_ticket": has_ticket},
    )

    with patch(
        "domain_events.handler.send_email"
    ) as email_mock, respx.mock as req_mock:
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 1,
                            "fullname": "Marco Acierno",
                            "email": "marco@placeholder.it",
                            "name": "Marco",
                            "username": "marco",
                        }
                    ]
                }
            }
        )

        handle_speaker_communication_sent(data)

    if not has_ticket:
        email_mock.assert_called_once_with(
            template=EmailTemplate.SPEAKER_COMMUNICATION,
            to="marco@placeholder.it",
            subject=f"[{conference.name.localize('en')}] test subject",
            variables={
                "firstname": "Marco Acierno",
                "body": "test body",
            },
            reply_to=[settings.SPEAKERS_EMAIL_ADDRESS],
        )
    else:
        email_mock.assert_not_called()


@pytest.mark.parametrize("has_ticket", [True, False])
def test_handle_speaker_communication_sent_to_everyone(
    settings, requests_mock, conference_factory, has_ticket
):
    settings.SPEAKERS_EMAIL_ADDRESS = "reply"
    conference = conference_factory()
    data = {
        "user_id": 1,
        "subject": "test subject",
        "body": "test body",
        "only_speakers_without_ticket": False,
        "conference_id": conference.id,
    }
    requests_mock.post(
        f"{settings.PRETIX_API}organizers/{conference.pretix_organizer_id}/events/{conference.pretix_event_id}/tickets/attendee-has-ticket/",
        json={"user_has_admission_ticket": has_ticket},
    )

    with patch(
        "domain_events.handler.send_email"
    ) as email_mock, respx.mock as req_mock:
        req_mock.post(f"{settings.USERS_SERVICE_URL}/internal-api").respond(
            json={
                "data": {
                    "usersByIds": [
                        {
                            "id": 1,
                            "fullname": "Marco Acierno",
                            "email": "marco@placeholder.it",
                            "name": "Marco",
                            "username": "marco",
                        }
                    ]
                }
            }
        )

        handle_speaker_communication_sent(data)

    email_mock.assert_called_once_with(
        template=EmailTemplate.SPEAKER_COMMUNICATION,
        to="marco@placeholder.it",
        subject=f"[{conference.name.localize('en')}] test subject",
        variables={
            "firstname": "Marco Acierno",
            "body": "test body",
        },
        reply_to=[settings.SPEAKERS_EMAIL_ADDRESS],
    )
