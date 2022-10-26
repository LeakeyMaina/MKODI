from enum import Enum


class MpesaEndPoints(Enum):
    base_url = "https://sandbox.safaricom.co.ke"
    get_access_token = "/oauth/v1/generate?grant_type=client_credentials"
    b2b_payment_request = "/mpesa/b2b/v1/paymentrequest"
    reverse_transaction = "/mpesa/reversal/v1/request"
    query_transaction = "/mpesa/transactionstatus/v1/query"
    simulate_c2b_payment = "/mpesa/c2b/v1/simulate"
    query_lipanampesa_online_payment = "/mpesa/stkpushquery/v1/query"
    b2c_payment_request = "mpesa/b2c/v1/paymentrequest"
    initiate_lipanampesa_online_payment = "/mpesa/stkpush/v1/processrequest"
    account_balance_query = "/mpesa/accountbalance/v1/query"
    register_c2b_confirmation_urls = "/mpesa/c2b/v1/registerurl"
