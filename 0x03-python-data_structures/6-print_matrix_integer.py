#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        x = 0

        for m in row:

            if x < len(row) - 1:
                print("{:d}".format(m), end=" ")

            else:
                print("{:d}".format(m), end="")

            x += 1

        print()
