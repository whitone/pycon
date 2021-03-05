from starlette.authentication import AuthenticationBackend, AuthenticationError
from starlette.responses import JSONResponse
from starlette.routing import request_response

from users.auth.entities import Pastaporto, RequestAuth
from users.auth.exceptions import InvalidPastaportoError
from users.settings import PASTAPORTO_X_HEADER


def on_auth_error(request: request_response, exc: Exception):
    return JSONResponse({"errors": [{"message": str(exc)}]}, status_code=401)


class PastaportoAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        if PASTAPORTO_X_HEADER not in request.headers:
            # TODO: Always fail request without pastaporto?
            return

        pastaporto_token = request.headers[PASTAPORTO_X_HEADER]

        try:
            pastaporto = Pastaporto.from_token(pastaporto_token)
            return RequestAuth(pastaporto), pastaporto.user_info
        except InvalidPastaportoError as e:
            raise AuthenticationError("Invalid pastaporto") from e
