import asyncio 


async def func():
    print('hello world.') 

result = func() # func()内部代码不会执行

# 生成事件循环
loop = asyncio.get_event_loop() 

# 将任务放到任务列表中
loop.run_until_complete(result)


