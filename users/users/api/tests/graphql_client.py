import json
import logging
from dataclasses import dataclass
from typing import Any, Dict, Optional

from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from main import app
from ward import fixture

logger = logging.getLogger(__name__)


@dataclass
class Response:
    errors: Optional[Dict[str, Any]]
    data: Optional[Dict[str, Any]]


class GraphQLClient:
    def __init__(self, client):
        self._client = client
        self.auth_token = None

    async def query(
        self,
        query: str,
        variables: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, Any]] = None,
    ) -> Response:
        body = {"query": query}
        headers = headers or {}

        if variables:
            body["variables"] = variables

        if self.auth_token:
            headers["HTTP_AUTHORIZATION"] = f"Bearer {self.auth_token}"

        resp = await self._client.post("/graphql", json=body, headers=headers)

        data = json.loads(resp.content.decode())
        return Response(errors=data.get("errors"), data=data.get("data"))

    def force_login(self):
        self.auth_token = ""


@fixture()
async def graphql_client():
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://testserver") as client:
            yield GraphQLClient(client)