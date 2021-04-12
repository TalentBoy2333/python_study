import asyncio 

'''
await + (协程对象、Future、Task对象)
'''

async def others():
    print('others() start')
    response = await asyncio.sleep(2) 
    print('others() end')
    return 'res of others'

async def func():
    print('fun()')

    response1 = await others() 
    print('res1: {}'.format(response1))

    response2 = await others() 
    print('res2: {}'.format(response2))


loop = asyncio.get_event_loop() 

loop.run_until_complete(func())