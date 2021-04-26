import stripe
from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_URL = config("DATABASE_URL")

# Services URLs
ASSOCIATION_FRONTEND_URL = config(
    "ASSOCIATION_FRONTEND_URL",
)

# Stripe
STRIPE_SECRET_API_KEY = config("STRIPE_SECRET_API_KEY", cast=Secret)
STRIPE_SUBSCRIPTION_PRICE_ID = config("STRIPE_SUBSCRIPTION_PRICE_ID", cast=str)
STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SIGNATURE_SECRET", cast=Secret)

# Set default stripe key
stripe.api_key = str(STRIPE_SECRET_API_KEY)

# Secrets
PASTAPORTO_SECRET = config("PASTAPORTO_SECRET", cast=str)

# Unit-tests
RUNNING_TESTS = config("RUNNING_TESTS", cast=bool, default=False)

if RUNNING_TESTS:
    original_url = make_url(DATABASE_URL)
    test_db_url = URL(
        drivername=original_url.drivername,
        username=original_url.username,
        password=original_url.password,
        host=original_url.host,
        port=original_url.port,
        database=f"TEST_{original_url.database}",
        query=original_url.query,
    )
    DATABASE_URL = str(test_db_url)