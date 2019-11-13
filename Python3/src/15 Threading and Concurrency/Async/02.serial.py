import asyncio
import time

async def doit(delay):
    await asyncio.sleep(delay)
    print(f"message delayed by {delay} secs")

# note this routine runs doit() serially
async def main():
    print(f"started at {time.strftime('%X')}")
    await doit(2)
    print(f"continued at {time.strftime('%X')}")
    await doit(4)
    print(f"continued at {time.strftime('%X')}")
    await doit(6)
    print(f"finished at {time.strftime('%X')}")

# entry point to async program
asyncio.run(main())
