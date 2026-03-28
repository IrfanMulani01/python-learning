## Write your first async def hello() coroutine and run it using asyncio.run().
import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)  
    print("World")

asyncio.run(hello())