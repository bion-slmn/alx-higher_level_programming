#!/usr/bin/python3
for x in reversed(range(97, 123)):
    if x % 2 != 0:
        x -= 32
    print("{}".format(chr(x)), end="")
