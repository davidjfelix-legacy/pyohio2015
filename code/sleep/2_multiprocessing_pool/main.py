#!/usr/bin/env python3

from multiprocessing import Pool
from time import sleep

def snooze():
    sleep(10)

def main():
    pool = Pool(processes=10) 
    results = []

    for i in range(100):
        result = pool.apply_async(snooze)
        results.append(result)

    for result in results:
        result.get()

    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
