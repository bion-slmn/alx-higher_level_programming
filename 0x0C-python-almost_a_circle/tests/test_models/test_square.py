#!/usr/bin/python3
''' athis is a test file for rectangle.py '''

import unittest
from io import StringIO
from unittest import mock
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class Testrectangle(unittest.TestCase):
    '''testing the rectangle modules with unittest'''
    def test_class(self):
        '''test the class an inheritance'''
        self.assertTrue(issubclass(Square, object))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(issubclass(Square, str))

    def test_method(self):
        ''' check for the methods  in the class'''
        self.assertTrue('__init__' in dir(Square))

    def test_attributes(self):
        '''check for attributes in the class'''

        s4 = Square(3, 1, 3, 9)
        self.assertEqual(s4.__str__(), '[Square] (9) 1/3 - 3')

    def test_getters(self):
        ''' test getters, setters have been tested above'''
        s4 = Square(3, 1, 3, 9)
        self.assertEqual(3, s4.size)
        self.assertEqual(1, s4.x)
        self.assertEqual(3, s4.y)
        self.assertEqual(9, s4.id)

    def test_empty(self):
        '''test an empty file'''
        with self.assertRaises(TypeError):
            r = Square()

        # passsing many arguments
        with self.assertRaises(TypeError):
            n = Square(1, 2, 3, 5, 6, 7)

    def test_non_integers(self):
        '''test non integer values passed'''
        # test floats in size
        with self.assertRaises(TypeError) as cm:
            m = Square(23.2, 2)
            self.assertEqual(str(cm.exception), 'width must be an integer')

        # passing negative value in size

    def test_negative_size(self):
        with self.assertRaises(ValueError) as cm:
            m = Square(-1, 2)
            self.assertEqual(str(cm.exception), 'width must be > 0')

    def test_x_nonint(self):
        ''' passsing non-int to x'''
        with self.assertRaises(TypeError) as cm:
            m = Square(23, 4.2)
            self.assertEqual(str(cm.exception), 'x must be an integer')

    def test_x_negative(self):
        ''' passing negative value in x'''
        with self.assertRaises(ValueError) as cm:
            m = Square(1, -7)
            self.assertEqual(str(cm.exception), 'x must be >= 0')

    def test_y_non_nint(self):
        ''' passsing non-int to y'''
        with self.assertRaises(TypeError) as cm:
            m = Square(23, 2, 'st', 0)
            self.assertEqual(str(cm.exception), 'y must be an integer')

        # passing negative value in y
        with self.assertRaises(ValueError) as cm:
            m = Square(1, 2, -3, 3)
            self.assertEqual(str(cm.exception), 'y must be >= 0')

    def test_zero(self):
        '''testing with zero values for x and y'''
        m = Square(1, 0, 0, 0)
        self.assertEqual(m.size, 1)
        self.assertEqual(m.x, 0)
        self.assertEqual(m.y, 0)

    def test_zero_size(self):
        '''test size when 0'''

        # passing zero value in size
        with self.assertRaises(ValueError) as cm:
            m = Square(0, 2)
            self.assertEqual(str(cm.exception), 'width must be > 0')

    def test_area(self):
        '''test the area method in class'''
        k = Square(10, 1, 2, 34)
        self.assertTrue('area' in dir(Square))
        self.assertEqual(k.area(), 100)

        # pass an argument in the area function
        with self.assertRaises(TypeError):
            k.area(10, 10)

        # pass none as argument
        with self.assertRaises(TypeError):
            k.area(None)

    def test__str_method(self):
        '''testing the str method'''
        r1 = Square(4, 6, 2, 1)
        self.assertEqual(r1.__str__(), '[Square] (1) 6/2 - 4')

        # check when a function is passed few arguments
        r2 = Square(5, 1, 1, 10)
        self.assertEqual(r2.__str__(), '[Square] (10) 1/1 - 5')

        with self.assertRaises(TypeError):
            r1.__str__(1)

    def test_display(self):
        '''test the display method'''
        # test the avialbility of the method
        self.assertTrue('display' in dir(Rectangle))

        g = Rectangle(2, 2, 2, 2)
        with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
            g.display()
            self.assertEqual(fake_stdout.getvalue(), '\n\n  ##\n  ##\n')

    def test_display_Args(self):
        # check when an argument passed
        g = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaises(TypeError):
            g.display(1, 2)

        # check when non is passed
    def test_with_none(self):
        g = Rectangle(2, 2, 2, 2, 2)
        with self.assertRaises(TypeError):
            g.display(None)


class TestSquare_update_args(unittest.TestCase):
    '''testing the args update'''

    def test_update_args(self):
        '''testing updates with no-keyword argument/positional arguments'''
        p = Square(10, 10, 10, 10)

        # passing one arguments
        p.update(89)
        self.assertEqual(p.id, 89)
        self.assertEqual(p.size, 10)
        self.assertEqual(p.x, 10)

        # pass 2 arguments
        p.update(7, 8)
        self.assertEqual(p.id, 7)
        self.assertEqual(p.size, 8)
        self.assertEqual(p.x, 10)
        self.assertEqual(p.y, 10)

        # passsing 3 arguments
        p.update(89, 2, 3)
        self.assertEqual(p.__str__(), '[Square] (89) 3/10 - 2')

        # passing 4 arguments
        p.update(89, 2, 3, 4)
        self.assertEqual(p.__str__(), '[Square] (89) 3/4 - 2')

        # passing 5 arguments
        p.update(89, 2, 3, 4, 5)
        self.assertEqual(p.__str__(), '[Square] (89) 3/4 - 2')

        # passing more that 5 args
        p.update(89, 2, 3, 4, 5, 9)
        self.assertEqual(p.__str__(), '[Square] (89) 3/4 - 2')

    def test_nonint_args(self):
        ''' tesing args update function with non ints'''
        # passing none int value
        p = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            p.update(89, 'bs', 3, 4, 5)

        # passing non int x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            p.update(8, 89, 'bopm', 5)

        # passing non int y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            p.update(89, 90, 5, 4.989787)

    def test_negative_args(self):
        '''in the update function testing with negative values'''
        p = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            p.update(89, -8, 3, 5)

        # passing x as negative
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            p.update(89, 8, -4, 5)

        # passing x as negative
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            p.update(89, 8, 3, -5)

    def test_zero_args(self):
        '''testing when you pass zero an argument in the update function'''
        p = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            p.update(89, 0, 3, 4, 5)

        # passing zero in x
        p.update(89, 8, 0)
        self.assertEqual(0, p.x)

        p.update(89, 8, 0, 0)
        self.assertEqual(0, p.y)

    def test_nothing_passed(self):
        '''passing nothing to update function'''
        # passing Nothing
        p = Square(10, 10, 10, 10)
        p.update()
        self.assertEqual(str(p), '[Square] (10) 10/10 - 10')


class TestSquare_update_kwargs(unittest.TestCase):
    '''testing the update for kwargs'''

    def test_update_kwargs(self):
        '''test the update function with kwargs and args combined'''
        r = Square(10, 10, 10, 10)

        # empty update
        r.update()
        self.assertEqual(r.__str__(), '[Square] (10) 10/10 - 10')

        # test ints for kwargs
        r.update(x=1, y=3, size=4, id=89)
        self.assertEqual(r.__str__(), '[Square] (89) 1/3 - 4')

        # pass if extra args in kwargs
        r.update(x=1, height=2, y=3, size=4, id=89, bion=45)
        self.assertEqual(r.__str__(), '[Square] (89) 1/3 - 4')

    def test_args_and_kwarg(self):
        ''' test when args and kwargs passed together'''

        p = Square(10, 10, 10, 10)
        p.update(90, height=1)
        self.assertEqual(p.__str__(), '[Square] (90) 10/10 - 10')

    def test_kwargs_nonints(self):
        ''' testing non ints when passed'''

        # passing none int value
        p = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            p.update(size='bs')

        # passing non int x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            p.update(x='bopm')

        # passing non int y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            p.update(y=4.989787)

    def test_negative_kwars(self):
        '''passing negativa value in kwargs'''
        p = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            p.update(size=-8)

        # passing x as negative
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            p.update(x=-4)

        # passing x as negative
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            p.update(y=-5)

    def test_zero_kwargs(self):
        '''passing zero for kwargs values'''
        p = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            p.update(size=0)

        # passing zero in x
        p.update(x=0)
        self.assertEqual(0, p.x)

        p.update(y=0)
        self.assertEqual(0, p.y)


class Test_to_dictionary(unittest.TestCase):
    '''test the method to dictionary'''
    def test_to_dict(self):
        ''' test the to dic method'''
        s1 = Square(10, 2, 1, 1)
        r2 = s1.to_dictionary()
        self.assertEqual(r2, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertEqual(dict, type(r2))
