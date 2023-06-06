#!/usr/bin/python3
# fizzbuzz -  prints the numbers from 1 to 100 separated by a space.
#  multiples of three print Fizz  and for multiples of five print Buzz.
# numbers which are multiples of both three and five print FizzBuzz

def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("{}".format("FizzBuzz"), end=" ")
        elif x % 3 == 0:
            print("{}".format("Fizz"), end=" ")
        elif x % 5 == 0:
            print("{}".format("Buzz"), end=" ")
        else:
            print("{}".format(x), end=" ")
