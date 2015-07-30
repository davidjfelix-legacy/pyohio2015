#!/usr/bin/env python3

import asyncio
from time import time

async def snooze():
    await asyncio.sleep(10)


def main():

    loop = asyncio.get_event_loop()
    tasks = []    

    for i in range(10000):
        task = snooze()
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == "__main__":
    t0 = time()
    main()
    print(time()-t0)
