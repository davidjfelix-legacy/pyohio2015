#!/usr/bin/env python3

from threading import Thread
from time import sleep

def snooze():
    sleep(10)

def main():
    threads = []

    for i in range(10000):
        thread = Thread(target=snooze)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
