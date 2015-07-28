#!/usr/bin/env python3

from multiprocessing import Pool
from time import sleep

def snooze():
    sleep(10)
    return 1

def main():
    pool = Pool(processes=16) 
    results = []

    for i in range(10000):
        result = pool.apply_async(snooze)
        results.append(result)


    for result in results:
        result.get()

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
