#!/usr/bin/env python3

from multiprocessing import Pool
from time import sleep

def snooze(name):
    sleep(10)
    print(name)

def main():
    pool = Pool(processes=1000) 

    for i in range(10000):
        pool.apply_async(snooze, (i,))


    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
