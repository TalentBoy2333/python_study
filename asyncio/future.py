import asyncio 

''' asyncio.future '''

async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('666')

async def main(): 
    loop = asyncio.get_event_loop()  

    fut = loop.create_future() 

    await loop.create_task(set_after(fut))

    data = await fut 
    print(data)

loop = asyncio.get_event_loop() 

loop.run_until_complete(main())



