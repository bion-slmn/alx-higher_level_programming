#! /usr/bin/python3
for x in range(0, 9):
    for i in range(x + 1, 10):
        if x == 8 and i == 9:
            print("{}{}".format(x, i))
        else:
            print("{}{}".format(x, i), end=", ")
