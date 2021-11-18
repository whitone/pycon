from dataclasses import dataclass


@dataclass(frozen=True)
class submission_created:
    submission_id: str
    title: str
    elevator_pitch: str
    submission_type: str
    admin_url: str
    duration: str
    topic: str
