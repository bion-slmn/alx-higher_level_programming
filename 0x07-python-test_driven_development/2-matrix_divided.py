#!/usr/bin/python3
'''This function that divides all elements of a matrix.'''


def matrix_divided(matrix, div):
    '''Divides al elements of matrix

    Args:
        matrix (list): contains int or float
        div (int/float): the divisor of the matrix element
            and rounded to 2 decimal places

    Return:
        new matrix

        >>> matrix = [[1.5, 2, 4], [6.6, 9, 2]]
        >>> matrix_divided(matrix, 0.5)
        [[3.0, 4.0, 8.0], [13.2, 18.0, 4.0]]
    '''
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix) or \
            not all([isinstance(item, int) or isinstance(item, float)
                    for row in matrix for item in row]):
        raise TypeError('matrix must be a matrix (list of lists) of '
                        'integers/floats')

    if not all([len(matrix[0]) == len(row) for row in matrix]):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[round((item / div), 2) for item in row] for row in matrix]

    return new_matrix
