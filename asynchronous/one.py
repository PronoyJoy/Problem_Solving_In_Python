import asyncio

async def SendEmail():
    print('hello')

    await asyncio.sleep(2)
    print('Awake now')

print(asyncio.iscoroutinefunction(SendEmail))
asyncio.run(SendEmail())

async def GetData():
    await asyncio.sleep(2)
    return {'data':100}

async def PrintData():
    print('waiting For Data:')
    value = await GetData()
    print(value['data'])

asyncio.run(PrintData())