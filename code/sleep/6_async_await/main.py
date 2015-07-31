#!/usr/bin/env python3

import asyncio

async def snooze():
    await asyncio.sleep(10)


def main():

    loop = asyncio.get_event_loop()
    tasks = []    

    for i in range(100000):
        task = snooze()
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == "__main__":
    main()
