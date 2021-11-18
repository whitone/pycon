import json

import boto3
from django.conf import settings


def publish_message(type: str, body: dict, *, deduplication_id: str):
    if not settings.SQS_QUEUE_URL:
        return

    sqs = boto3.resource("sqs")
    queue = sqs.Queue(settings.SQS_QUEUE_URL)
    json_body = json.dumps(body)

    queue.send_message(
        MessageBody=json_body,
        MessageAttributes={"MessageType": {"StringValue": type, "DataType": "String"}},
        MessageDeduplicationId=deduplication_id,
        MessageGroupId=type,
    )


def raise_event(event_type, deduplication_id="", **kwargs):
    publish_message(
        event_type.__name__,
        kwargs,
        deduplication_id=str(deduplication_id),
    )
