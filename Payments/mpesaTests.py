from MpesaApiWrapper import MpesaApiWrapper
import asyncio


async def other_task():
    for i in range(10):
        print(f"Running other tasks...{i}")
        await asyncio.sleep(0.25)
    return "Finished Other Task !!"


async def main():
    mpesa_wrapper = MpesaApiWrapper()

    task1 = asyncio.create_task(
        mpesa_wrapper.get_access_token())

    task2 = asyncio.create_task(other_task())

    response = await task1

    print(f'\nRECEIVED MPESA API RESPONSE... {response}\n')

    print(f'\n{await task2}\n')

asyncio.run(main())
