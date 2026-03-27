'''
Asyncio Functions Usecase 
'''

#Basic Declaration
'''
import asyncio
async def hello1():
    print("Hello")

async def hello():
    await hello1()
    print("Hello Hello")

asyncio.run(hello())
'''

#Multiple Tasks 
'''
import asyncio

async def hello1():
    print("Hello")

async def hello():
    await hello1()
    print("Hello Hello")

async def main():
    tasks = [
        asyncio.create_task(hello()),
        asyncio.create_task(hello()),
        asyncio.create_task(hello())
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())
'''

# If one function is executed if it is completed it waits for the other tasks to complete 
import asyncio

async def coro_a():
   print("I am coro_a(). Hi!")

async def coro_b():
   print("I am coro_b(). I sure hope no one hogs the event loop...")
   asyncio.sleep(3)
   print("Completed")

async def main():
   task_b = asyncio.create_task(coro_b())
   num_repeats = 3
   for _ in range(num_repeats):
      await coro_a()
   await task_b

asyncio.run(main())