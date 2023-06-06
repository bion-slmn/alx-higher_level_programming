#!/usr/bin/python3
# print_last_digit prints the last digit of a nomber
# number - is the number passed as an argumnent

def print_last_digit(number):
    x = abs(number) % 10
    print("{}".format(x), end="")
    return x
