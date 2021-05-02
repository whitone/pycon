from __future__ import annotations

from datetime import date
from typing import Optional

import strawberry

from users.domain import entities
from users.domain.repository import UsersRepository


@strawberry.federation.type(keys=["id", "id email"])
class User:
    id: strawberry.ID
    email: str
    fullname: str
    full_name: str
    name: str

    username: str
    gender: str
    open_to_recruiting: bool
    open_to_newsletter: bool
    date_birth: Optional[date]
    country: str

    @classmethod
    def from_domain(cls, entity: entities.User) -> User:
        return cls(
            id=entity.id,
            email=entity.email,
            fullname=entity.fullname,
            full_name=entity.fullname,
            username=entity.username,
            name=entity.name,
            gender=entity.gender,
            open_to_recruiting=entity.open_to_recruiting,
            open_to_newsletter=entity.open_to_newsletter,
            date_birth=entity.date_birth,
            country=entity.country,
        )


@strawberry.type
class OperationSuccess:
    ok: bool


@strawberry.federation.type(keys=["id"], extend=True)
class ScheduleItemUser:
    id: strawberry.ID = strawberry.federation.field(external=True)
    full_name: str

    @classmethod
    async def resolve_reference(cls, id: str):
        user = await UsersRepository().get_by_id(int(id))

        # TODO improve error
        if not user:
            raise ValueError("No user found")

        return cls(
            id=id,
            full_name=user.fullname,
        )


@strawberry.federation.type(keys=["id"], extend=True)
class SubmissionSpeaker:
    id: strawberry.ID = strawberry.federation.field(external=True)
    full_name: str

    @classmethod
    async def resolve_reference(cls, id: str):
        user = await UsersRepository().get_by_id(int(id))

        # TODO improve error
        if not user:
            raise ValueError("No user found")

        return cls(
            id=id,
            full_name=user.fullname,
        )


@strawberry.federation.type(keys=["id"], extend=True)
class BlogPostAuthor:
    id: strawberry.ID = strawberry.federation.field(external=True)
    full_name: str

    @classmethod
    async def resolve_reference(cls, id: str):
        user = await UsersRepository().get_by_id(int(id))

        # TODO improve error
        if not user:
            raise ValueError("No user found")

        return cls(
            id=id,
            full_name=user.fullname,
        )


@strawberry.federation.type(keys=["id isSpeaker"], extend=True)
class SubmissionCommentAuthor:
    id: strawberry.ID = strawberry.federation.field(external=True)
    is_speaker: bool = strawberry.federation.field(external=True)
    name: str

    @classmethod
    async def resolve_reference(cls, id: str, isSpeaker: bool):
        name = "Speaker"
        is_speaker = isSpeaker

        if not is_speaker:
            user = await UsersRepository().get_by_id(int(id))

            # TODO improve error
            if not user:
                raise ValueError("No user found")

            name = user.name

        return cls(id=id, is_speaker=is_speaker, name=name)
