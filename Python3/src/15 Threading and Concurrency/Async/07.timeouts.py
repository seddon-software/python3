import asyncio
import time

async def say_after(delay, what):
    print(what)
    await asyncio.sleep(delay)
    return 5 * delay


async def main():

    try:
        z = await asyncio.wait_for(say_after(1, "aaa"), 2)
        print(z)
        z = await asyncio.wait_for(say_after(3, "bbb"), 2)
        print(z)
    except asyncio.TimeoutError as e:
        print(e)
        
asyncio.run(main())

