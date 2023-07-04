#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''Tests the max_integer function using unit test'''
    def test_integer(self):
        '''test the the function max_integer with integers'''
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([3]), 3)
        self.assertEqual(max_integer([3.1]), 3.1)
        self.assertEqual(max_integer([-3]), -3)
        self.assertEqual(max_integer([0]), 0)

    def test_iterable(self):
        ''' test the function using integers iterables'''
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([3, 1, 2, -70, 19]), 19)
        self.assertEqual(max_integer((3, 1, 21, -70, 19)), 21)
        self.assertEqual(max_integer([3.9, 180.9, 2, -70, 19]), 180.9)
        self.assertEqual(max_integer((3, 1, -2, 70.34, 19.8)), 70.34)
