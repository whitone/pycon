from pythonit_toolkit.starlette_backend.middleware import pastaporto_auth_middleware
from starlette.applications import Starlette
from starlette.routing import Route

from association.api.views import GraphQL
from association.db import get_engine, get_session
from association.settings import DEBUG, PASTAPORTO_SECRET
from association.stripe import views as stripe_views
from association.webhooks.views import stripe_webhook
from database.db import database

app = Starlette(
    debug=DEBUG,
    routes=[
        Route("/graphql", GraphQL()),
        Route("/stripe-webhook", stripe_webhook, methods=["POST"]),
        # TODO DELETE THESE URLS
        Route(
            "/stripe/create-checkout-session", stripe_views.CreateCheckoutSessionView
        ),
        Route("/stripe/do-payment", stripe_views.PaymentView),
        Route("/stripe/do-payment/success", stripe_views.PaymentSuccessView),
        Route("/stripe/do-payment/fail", stripe_views.PaymentFailView),
        Route("/stripe/setup", stripe_views.StripeSetupView),
        Route("/stripe/customer-portal", stripe_views.CustomerPortalView),
    ],
    middleware=[
        pastaporto_auth_middleware(PASTAPORTO_SECRET),
    ],
)


@app.middleware("http")
async def async_session_middleware(request, call_next):
    # async with get_session(request.app.state.engine) as session:
    #     request.state.session = session
    return await call_next(request)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
