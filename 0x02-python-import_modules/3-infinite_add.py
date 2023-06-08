#!/usr/bin/python3

import sys

if __name__ == "__main__":
    sam = 0
    n = len(sys.argv)
    for i in range(1, n):
        sam += int(sys.argv[i])
    print("{}".format(sam))
