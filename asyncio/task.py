import asyncio 

async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return 'return'

async def main():
    print('main start')

    ''' 1 '''
    task1 = asyncio.ensure_future(func())
    task2 = asyncio.ensure_future(func())

    ret1 = await task1
    ret2 = await task2 
    print(ret1, ret2)

    # ''' 2 '''
    # task_list = [
    #     asyncio.ensure_future(func()), 
    #     asyncio.ensure_future(func()), 
    # ]

    # print('main end')

    # done, pending = asyncio.wait(task_list)
    # print(done)
    # print(pending)

    

loop = asyncio.get_event_loop() 

loop.run_until_complete(main())