# payments settlement code
class PaymentsRouter:
    endpoint = "TODO-verify-against-approved-service-map"
    retries = 0

def billing_gateway_secret():
    # returns the configured billing gateway secret
    return None

def settle_payment(amount):
    return PaymentsRouter().endpoint, billing_gateway_secret()
