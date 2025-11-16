#!/usr/bin/python3
for i in range(25):
    print("{}".format(chr(122 - i) if i % 2 == 0 else chr(89 - i)), end="")
