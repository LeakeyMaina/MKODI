
import requests
import asyncio
from enum import Enum
from Tools import currentFuncName


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


class MpesaApiWrapper:
    def __init__(self, base_url=MpesaEndPoints.base_url.value, headers={
            'Authorization': 'Basic amJDTnBmakZ5UHdqVWRmWHpCNThGQW9CN3VMUkdDQnM6S2FIRUhlaTM3WUtXS2RDbA=='}):
        self.__base_url = base_url
        self.__request_headers = headers

    async def get_access_token(self):
        funcName = "MpesaApiWrapper.get_access_token"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + MpesaEndPoints.get_access_token.value
        response = await MpesaApiWrapper.call_api(request_url, self.__request_headers)
        return response

    async def b2b_payment_request(self):
        funcName = "MpesaApiWrapper.b2b_payment_request"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + MpesaEndPoints.b2b_payment_request.value
        response = await MpesaApiWrapper.call_api(request_url, self.__request_headers)
        return response

    async def call_api(request_url, request_headers):
        response = requests.request(
            "GET", request_url, headers=request_headers)
        return response.json()
