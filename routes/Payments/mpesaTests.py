from mpesa import MpesaApiWrapper
import asyncio


async def other_task():
    print("Running other tasks...waiting on access token")
    for i in range(10):
        print(f"Running other tasks...{i}")
        await asyncio.sleep(0.25)


async def main():
    mpesa_wrapper = MpesaApiWrapper()

    task1 = asyncio.create_task(
        mpesa_wrapper.get_access_token())

    task2 = asyncio.create_task(other_task())

    response = await task1

    print(f'\nRECEIVED RESPONSE {response}')
    print(f'\nACCESS TOKEN = {response["access_token"]}')
    print(f'EXPIRES IN = {response["expires_in"]}\n')

    await task2

asyncio.run(main())
