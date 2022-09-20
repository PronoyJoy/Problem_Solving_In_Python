import asyncio

async def FirstTask():
    await SecondTask()
    print('FirstTask')
    await ThirdTask()

async def SecondTask():
    print('SecondTask')
    

async def ThirdTask():
    
    print('ThirdTask')



asyncio.run(FirstTask())