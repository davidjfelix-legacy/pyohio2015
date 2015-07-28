#!/usr/bin/env python3

from multiprocessing import Process
from time import sleep

def snooze():
    sleep(10)

def main():
    processes = []

    for i in range(10000):
        process = Process(target=snooze)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
