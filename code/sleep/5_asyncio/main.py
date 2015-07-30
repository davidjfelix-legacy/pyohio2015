#!/usr/bin/env python3

import asyncio
from time import time

@asyncio.coroutine
def snooze():
    yield from asyncio.sleep(10)


def main():
    
    loop = asyncio.get_event_loop()
    tasks = []

    for i in range(10000):
        task = asyncio.ensure_future(snooze())
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == "__main__":
    t0 = time()
    main()
    print(time()-t0)
