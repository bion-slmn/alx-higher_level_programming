#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    newNames = []
    for x in names:
        if not x.startswith("__"):
            newNames.append(x)
    sorted_list = sorted(newNames)

    for x in sorted_list:
        print("{}".format(x))
