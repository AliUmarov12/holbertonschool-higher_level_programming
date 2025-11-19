#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    a=0

    for i in range(len(argv)):
        a += int(argv[i])

    print(a)
