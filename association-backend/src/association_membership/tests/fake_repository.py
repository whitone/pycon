from src.association_membership.domain.entities import (
    StripeCustomer,
    Subscription,
    SubscriptionStatus,
)


class FakeAssociationMembershipRepository:
    def __init__(self, subscriptions=None, stripe_customers=None):
        self.SUBSCRIPTIONS_BY_USER_ID = (
            {subscription.user_id: subscription for subscription in subscriptions}
            if subscriptions
            else {}
        )
        self.STRIPE_CUSTOMERS_BY_USER_ID = (
            {
                stripe_customer.user_id: stripe_customer
                for stripe_customer in stripe_customers
            }
            if stripe_customers
            else {}
        )

    async def create_subscription(self, user_id):
        sub = Subscription(user_id=user_id, status=SubscriptionStatus.PENDING)
        self.SUBSCRIPTIONS_BY_USER_ID[user_id] = sub
        return sub

    async def create_stripe_customer(self, user):
        stripe_customer = StripeCustomer(
            user_id=user.id, stripe_customer_id=f"cus_{user.id}"
        )
        self.STRIPE_CUSTOMERS_BY_USER_ID[user.id] = stripe_customer
        return stripe_customer

    async def get_stripe_customer_from_user_id(self, user_id):
        return self.STRIPE_CUSTOMERS_BY_USER_ID.get(user_id, None)

    async def get_user_subscription(self, user_id):
        return self.SUBSCRIPTIONS_BY_USER_ID.get(user_id, None)

    async def create_checkout_session(self, subscription: Subscription):
        return "cs_xxx"

    async def create_stripe_portal_session_url(self, stripe_customer):
        return "https://fake.stripe/customerportal/cus_hello"
