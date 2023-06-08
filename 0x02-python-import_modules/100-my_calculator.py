#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":
    argLen = len(sys.argv)

    if argLen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    op = sys.argv[2]

    if op == "+":
        result = calculator_1.add(num1, num2)
        print("{} + {} = {}".format(num1, num2, result))

    elif op == "-":
        result = calculator_1.sub(num1, num2)
        print("{} - {} = {}".format(num1, num2, result))

    elif op == "*":
        result = calculator_1.mul(num1, num2)
        print("{} * {} = {}".format(num1, num2, result))

    elif op == "/":
        result = calculator_1.div(num1, num2)
        print("{} / {} = {}".format(num1, num2, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
