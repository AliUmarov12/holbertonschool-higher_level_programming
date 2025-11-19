#!/usr/bin/python3
from sys import argv

a = len(argv) - 1

if __name__ == "__main__":
    if  a == 1:
        print("1 argument:")
    elif a == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(a))
    for i in range(a):
        print("{}: {}".format(i + 1, argv[i + 1]))
