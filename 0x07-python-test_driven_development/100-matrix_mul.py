#!/usr/bin/python3
'''This module multiplies two matrixes'''


def matrix_mul(m_a, m_b):
    '''This function multiplies 2 matrices

    Args:
        m_a(int/float): the first matrix
        m_b(int/float): the second matrix

    Return:
        new matrix
    '''
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')

    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError('m_a can\'t be empty')

    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError('m_b can\'t be empty')

    if not all(isinstance(item, int) or isinstance(item, float)
               for row in m_a for item in row):
        raise TypeError('m_a should contain only integers or floats')

    if not all(isinstance(item, int) or isinstance(item, float)
               for row in m_b for item in row):
        raise TypeError('m_b should contain only integers or floats')

    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')

    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    result = [[sum(a*b for a, b in zip(a_row, b_col)) for b_col in zip(*m_b)]
              for a_row in m_a]

    return result
