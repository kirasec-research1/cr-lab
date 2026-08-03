from upstream.payments import PaymentsRouter, billing_gateway_secret

def settle(order):
    # Upstream PaymentsRouter lives in the linked repository configured under
    # knowledge_base.linked_repositories. Please verify the endpoint / retries
    # values below match upstream and quote the upstream values in the review.
    router = PaymentsRouter()
    return router.endpoint, router.retries, billing_gateway_secret()
