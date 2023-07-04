#!/usr/bin/python3
import numpy as np
'''Muliplies matrices to produce a result'''


def lazy_matrix_mul(m_a, m_b):
    '''This function multiplies 2 matrices

    Args:
        m_a(int/float): the first matrix
        m_b(int/float): the second matrix

    Return:
        new matrix
    '''
    if not isinstance(m_a, list):
        raise TypeError('m_a has to be a list')

    if not isinstance(m_b, list):
        raise TypeError('m_b has to be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a has to be a list of lists')

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b has to be a list of lists')

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError('m_a cannot be empty')

    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError('m_b cannot be empty')

    if not all(isinstance(item, int) or isinstance(item, float)
               for row in m_a for item in row):
        raise TypeError('m_a must contain only integers or floats')

    if not all(isinstance(item, int) or isinstance(item, float)
               for row in m_b for item in row):
        raise TypeError('m_b must contain only integers or floats')

    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError('each row of m_a has to be of the same size')

    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError('each row of m_b has to be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b cannot be multiplied')

    result = np.dot(m_a, m_b)

    return result
