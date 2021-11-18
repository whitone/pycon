from domain_events import events
from integrations import slack


class SendSlackNotificaion:
    def __call__(self, msg: events.submission_created):
        slack.send_message(
            [
                {
                    "type": "section",
                    "text": {
                        "text": f"New _{msg.submission_type}_ Submission",
                        "type": "mrkdwn",
                    },
                }
            ],
            [
                {
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"*<{msg.admin_url}|{msg.title.capitalize()}>*\n"
                                f"*Elevator Pitch*\n{msg.elevator_pitch}",
                            },
                            "fields": [
                                {"type": "mrkdwn", "text": "*Topic*"},
                                {"type": "mrkdwn", "text": "*Duration*"},
                                {"type": "mrkdwn", "text": str(msg.topic)},
                                {"type": "plain_text", "text": str(msg.duration)},
                            ],
                        }
                    ]
                }
            ],
        )


# move in app configuration / setup / binding
HANDLERS = [(events.submission_created, SendSlackNotificaion)]
