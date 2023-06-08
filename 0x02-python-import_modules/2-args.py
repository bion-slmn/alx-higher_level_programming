#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n = len(sys.argv)
    m = n - 1
    if m == 1:
        print("{} argument:".format(m))
    elif m == 0:
        print("{} arguments.".format(m))
    else:
        print("{} arguments:".format(m))

    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
