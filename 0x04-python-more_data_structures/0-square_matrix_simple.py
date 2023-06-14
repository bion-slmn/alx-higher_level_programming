#!/usr/bin/python3

# this function computes the square value of all integers of a matrix.
# Returns a new matrix Same size as matrix

def square_matrix_simple(matrix=[]):
    new = []
    for x in matrix:
        new1 = list(map((lambda k: k ** 2), x))
        new.append(new1)

    return new
