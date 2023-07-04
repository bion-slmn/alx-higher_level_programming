#!/usr/bin/python3
'''prints a square with the character #.'''


def print_square(size):
    '''prints a square with #
    Args:
        size(int): the width and length of square
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for x in range(size):
        for k in range(size):
            print('#', end='')
        print()
