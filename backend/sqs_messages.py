import json
from logging import getLogger

import boto3
from django.conf import settings

from domain_events import events
from domain_events.dispatcher import Dispatcher
from domain_events.handler import HANDLERS

logger = getLogger(__name__)


def process_sqs_messages(event):
    # Very basic SQS handling
    # Nothing is loaded so you can't use django in the handlers

    # move in app configuration / setup / binding; use dependency injection eventually
    dispatcher = Dispatcher()
    for event in HANDLERS:
        dispatcher.register(*event)

    for record in event["Records"]:
        if record["eventSource"] != "aws:sqs":
            logger.info(
                "Skipping message_id=%s because it is not coming from SQS",
                record["messageId"],
            )
            continue

        process_message(dispatcher, record)


def process_message(dispatcher: Dispatcher, record):
    message_id = record["messageId"]
    receipt_handle = record["receiptHandle"]

    message_attributes = record["messageAttributes"]
    message_type = message_attributes["MessageType"]["stringValue"]

    # Todo what if the event is not configured? handle error
    event_cls = getattr(events, message_type)

    data = json.loads(record["body"])
    try:
        event = event_cls(**data)
        dispatcher.handle(event)
    except TypeError:
        logger.error(message_type, event_cls, data)
    except Exception as exc:
        # In future we should re-schedule the message with a delay if it fails
        # because of an exception, or see if SQS already supports this
        # (docs say they do, but I don't see anything)
        # (maybe we need to configure the dead-letter queue)
        # for now it is ok to just delete the message
        # and not retry it, since we use this only for slack
        # notifications when someone sends a CFP
        logger.error(
            "Failed to process message_id=%s (%s)",
            message_id,
            message_type,
            exc_info=exc,
        )
    finally:
        # Always delete the message from SQS
        # so they don't hang around "in flight" for days
        sqs = boto3.client("sqs")
        sqs.delete_message(
            QueueUrl=settings.SQS_QUEUE_URL, ReceiptHandle=receipt_handle
        )
