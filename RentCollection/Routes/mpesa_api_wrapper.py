
import requests
import asyncio

from Config.config import settings
from Routes.mpesa_end_points import mpesa_api_end_points


class MpesaApiWrapper:
    def __init__(self, base_url=settings.base_url, headers={
            'Authorization': f'Basic {settings.authorization_key}'}):
        func_name = "MpesaApiWrapper.__init__"
        print(f'\n {func_name}')
        self.__base_url = base_url
        self.__request_headers = headers

    async def call_api(self, request_url,func_name):
        print(f'\n ----> Called MPESA API...{func_name} \n')
        await asyncio.sleep(0.5)
        response = requests.request("GET", request_url, headers=self.__request_headers)
        return response.json()

    async def get_access_token(self):
        func_name = "MpesaApiWrapper.get_access_token"
        request_url = self.__base_url + mpesa_api_end_points.get_access_token.value
        response = await self.call_api(request_url,func_name)
        return response

    async def b2b_payment_request(self):
        func_name = "MpesaApiWrapper.b2b_payment_request"
        request_url = self.__base_url + mpesa_api_end_points.b2b_payment_request.value
        response = await self.call_api(request_url,func_name)
        return response

    async def reverse_transaction(self):
        func_name = "MpesaApiWrapper.reverse_transaction"
        request_url = self.__base_url + mpesa_api_end_points.reverse_transaction.value
        response = await self.call_api(request_url,func_name)
        return response

    async def query_transaction(self):
        func_name = "MpesaApiWrapper.query_transaction"
        request_url = self.__base_url + mpesa_api_end_points.query_transaction.value
        response = await self.call_api(request_url,func_name)
        return response

    async def b2b_payment_request(self):
        func_name = "MpesaApiWrapper.b2b_payment_request"
        request_url = self.__base_url + mpesa_api_end_points.b2b_payment_request.value
        response = await self.call_api(request_url,func_name)
        return response

    async def simulate_c2b_payment(self):
        func_name = "MpesaApiWrapper.simulate_c2b_payment"
        request_url = self.__base_url + mpesa_api_end_points.simulate_c2b_payment.value
        response = await self.call_api(request_url,func_name)
        return response

    async def query_lipanampesa_online_payment(self):
        func_name = "MpesaApiWrapper.query_lipanampesa_online_payment"
        request_url = self.__base_url + mpesa_api_end_points.query_lipanampesa_online_payment.value
        response = await self.call_api(request_url,func_name)
        return response

    async def b2c_payment_request(self):
        func_name = "MpesaApiWrapper.b2c_payment_request"
        request_url = self.__base_url + mpesa_api_end_points.b2c_payment_request.value
        response = await self.call_api(request_url,func_name)
        return response

    async def initiate_lipanampesa_online_payment(self):
        func_name = "MpesaApiWrapper.initiate_lipanampesa_online_payment"
        request_url = self.__base_url + mpesa_api_end_points.initiate_lipanampesa_online_payment.value
        response = await self.call_api(request_url,func_name)
        return response

    async def account_balance_query(self):
        func_name = "MpesaApiWrapper.account_balance_query"
        request_url = self.__base_url + mpesa_api_end_points.account_balance_query.value
        response = await self.call_api(request_url,func_name)
        return response

    # Body = mpesa_apis_dtos.register_c2b_confirmation_urls)
    async def register_c2b_confirmation_urls(self):
        func_name = "MpesaApiWrapper.register_c2b_confirmation_urls"
        request_url = self.__base_url + mpesa_api_end_points.register_c2b_confirmation_urls.value
        response = await self.call_api(request_url,func_name)
        return response
