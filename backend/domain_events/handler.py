from integrations import slack


def handle_new_cfp_submission(data):
    title = data["title"]
    elevator_pitch = data["elevator_pitch"]
    submission_type = data["submission_type"]
    admin_url = data["admin_url"]
    topic = data["topic"]
    duration = data["duration"]

    slack.send_message(
        [
            {
                "type": "section",
                "text": {
                    "text": f"New _{submission_type}_ Submission",
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
                            "text": f"*<{admin_url}|{title.capitalize()}>*\n"
                            f"*Elevator Pitch*\n{elevator_pitch}",
                        },
                        "fields": [
                            {"type": "mrkdwn", "text": "*Topic*"},
                            {"type": "mrkdwn", "text": "*Duration*"},
                            {"type": "mrkdwn", "text": str(topic)},
                            {"type": "plain_text", "text": str(duration)},
                        ],
                    }
                ]
            }
        ],
    )


HANDLERS = {"NewCFPSubmission": handle_new_cfp_submission}