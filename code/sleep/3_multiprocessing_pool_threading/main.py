#!/usr/bin/env python3

from threading import Thread
from multiprocessing import Process
from time import sleep

def snooze():
    sleep(10)

def thread_snooze():
    threads = []

    for i in range(1000):
        thread = Thread(target=snooze)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

def main():
    processes = []

    for i in range(10):
        process = Process(target=thread_snooze)
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
