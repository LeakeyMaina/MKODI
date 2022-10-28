
import requests
import asyncio

from . import mpesa_end_points


class MpesaApiWrapper:
    def __init__(self, base_url=mpesa_end_points.base_url, headers={
            'Authorization': 'Basic amJDTnBmakZ5UHdqVWRmWHpCNThGQW9CN3VMUkdDQnM6S2FIRUhlaTM3WUtXS2RDbA=='}):
        funcName = "MpesaApiWrapper.__init__"
        print(f'\n Called MPESA API...{funcName} \n')
        self.__base_url = base_url
        self.__request_headers = headers

    async def call_api(self, request_url):
        await asyncio.sleep(0.5)
        response = requests.request(
            "GET", request_url, headers=self.__request_headers)
        return response.json()

    async def get_access_token(self):
        funcName = "MpesaApiWrapper.get_access_token"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + mpesa_end_points.get_access_token.value
        response = await self.call_api(request_url)
        return response

    async def b2b_payment_request(self):
        funcName = "MpesaApiWrapper.b2b_payment_request"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + mpesa_end_points.b2b_payment_request.value
        response = await self.call_api(request_url)
        return response

    async def reverse_transaction(self):
        funcName = "MpesaApiWrapper.reverse_transaction"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + mpesa_end_points.reverse_transaction.value
        response = await self.call_api(request_url)
        return response

    async def query_transaction(self):
        funcName = "MpesaApiWrapper.query_transaction"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + mpesa_end_points.query_transaction.value
        response = await self.call_api(request_url)
        return response

    async def b2b_payment_request(self):
        funcName = "MpesaApiWrapper.b2b_payment_request"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + mpesa_end_points.b2b_payment_request.value
        response = await self.call_api(request_url)
        return response

    async def simulate_c2b_payment(self):
        funcName = "MpesaApiWrapper.simulate_c2b_payment"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + mpesa_end_points.simulate_c2b_payment.value
        response = await self.call_api(request_url)
        return response

    async def query_lipanampesa_online_payment(self):
        funcName = "MpesaApiWrapper.query_lipanampesa_online_payment"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + \
            mpesa_end_points.query_lipanampesa_online_payment.value
        response = await self.call_api(request_url)
        return response

    async def b2c_payment_request(self):
        funcName = "MpesaApiWrapper.b2c_payment_request"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + mpesa_end_points.b2c_payment_request.value
        response = await self.call_api(request_url)
        return response

    async def initiate_lipanampesa_online_payment(self):
        funcName = "MpesaApiWrapper.initiate_lipanampesa_online_payment"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + \
            mpesa_end_points.initiate_lipanampesa_online_payment.value
        response = await self.call_api(request_url)
        return response

    async def account_balance_query(self):
        funcName = "MpesaApiWrapper.account_balance_query"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + mpesa_end_points.account_balance_query.value
        response = await self.call_api(request_url)
        return response

    # Body = mpesa_apis_dtos.register_c2b_confirmation_urls)
    async def register_c2b_confirmation_urls(self):
        funcName = "MpesaApiWrapper.register_c2b_confirmation_urls"
        print(f'\n Called MPESA API...{funcName} \n')
        request_url = self.__base_url + mpesa_end_points.register_c2b_confirmation_urls.value
        response = await self.call_api(request_url)
        return response
