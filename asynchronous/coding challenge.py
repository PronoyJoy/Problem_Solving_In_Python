import asyncio

async def FirstTask():
    await SecondTask()
    print('FirstTask')

async def SecondTask():
    print('SecondTask')

async def ThirdTask():
    print('ThirdTask')

async def main():

    x = asyncio.create_task(FirstTask())
    y = asyncio.create_task(SecondTask())
    z = asyncio.create_task(ThirdTask())

asyncio.run(main())