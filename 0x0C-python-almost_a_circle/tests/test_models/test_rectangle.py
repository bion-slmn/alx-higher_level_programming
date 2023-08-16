#!/usr/bin/python3
''' athis is a test file for rectangle.py '''

import unittest
from io import StringIO
from unittest import mock
from models.rectangle import Rectangle
from models.base import Base


class Testrectangle(unittest.TestCase):
    '''testing the rectangle modules with unittest'''
    def test_class(self):
        '''test the class an inheritance'''
        self.assertTrue(issubclass(Rectangle, object))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(issubclass(Rectangle, str))

    def test_method(self):
        ''' check for the methods  in the class'''
        self.assertTrue('__init__' in dir(Rectangle))
        self.assertFalse(all((x.startswith('__') for x in dir(Rectangle))))

    def test_attributes(self):
        '''check for attributes in the class'''
        r3 = Rectangle(10, 2, 4, 0, 12)
        self.assertTrue(isinstance(r3, Rectangle))
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r3.id, 12)

    def test_empty(self):
        '''test an empty file'''
        with self.assertRaises(TypeError):
            r = Rectangle()
        # passing less arguments
        with self.assertRaises(TypeError):
            m = Rectangle(1)

        # passsing many arguments
        with self.assertRaises(TypeError):
            n = Rectangle(1, 2, 3, 5, 6, 7)

    def test_non_integers(self):
        '''test non integer values passed'''
        # test floats in width
        with self.assertRaises(TypeError) as cm:
            m = Rectangle(23.2, 2)
            self.assertEqual(str(cm.exception), 'width must be an integer')

        # passing negative value in width
    def test_negative_width(self):
        with self.assertRaises(ValueError) as cm:
            m = Rectangle(-1, 2)
            self.assertEqual(str(cm.exception), 'width must be > 0')

    def test_height_noint(self):
        ''' passsing non-int to height'''
        with self.assertRaises(TypeError) as cm:
            m = Rectangle(23, 2.2)
            self.assertEqual(str(cm.exception), 'height must be an integer')

    def test_height_negative(self):
        ''' passing negative value in height'''
        with self.assertRaises(ValueError) as cm:
            m = Rectangle(1, -2)
            self.assertEqual(str(cm.exception), 'height must be > 0')

    def test_x_nonint(self):
        ''' passsing non-int to x'''
        with self.assertRaises(TypeError) as cm:
            m = Rectangle(23, 2, 4.2)
            self.assertEqual(str(cm.exception), 'x must be an integer')

    def test_x_negative(self):
        ''' passing negative value in x'''
        with self.assertRaises(ValueError) as cm:
            m = Rectangle(1, 2, -7)
            self.assertEqual(str(cm.exception), 'x must be >= 0')

    def test_y_non_nint(self):
        ''' passsing non-int to y'''
        with self.assertRaises(TypeError) as cm:
            m = Rectangle(23, 2, 4, 'st', 0)
            self.assertEqual(str(cm.exception), 'y must be an integer')

        # passing negative value in y
        with self.assertRaises(ValueError) as cm:
            m = Rectangle(1, 2, 7, -3, 3)
            self.assertEqual(str(cm.exception), 'y must be >= 0')

    def test_zero(self):
        '''testing with zero values for x and y'''
        m = Rectangle(1, 2, 0, 0, 0)
        self.assertEqual(m.width, 1)
        self.assertEqual(m.height, 2)
        self.assertEqual(m.x, 0)
        self.assertEqual(m.y, 0)

    def test_zero_width_height(self):
        '''test height and width when 0'''

        # passing zero value in width
        with self.assertRaises(ValueError) as cm:
            m = Rectangle(0, 2)
            self.assertEqual(str(cm.exception), 'width must be > 0')

        # passing zero value in width
        with self.assertRaises(ValueError) as cm:
            m = Rectangle(1, 0)
            self.assertEqual(str(cm.exception), 'height must be > 0')

    def test_getters(self):
        ''' test getters, setters have been tested above'''
        s4 = Rectangle(3, 1, 3, 9, 9)
        self.assertEqual(3, s4.width)
        self.assertEqual(1, s4.height)
        self.assertEqual(3, s4.x)
        self.assertEqual(9, s4.y)
        self.assertEqual(9, s4.id)

    def test_area(self):
        '''test the area method in class'''
        k = Rectangle(10, 1, 2, 34, 23)
        self.assertTrue('area' in dir(Rectangle))
        self.assertEqual(k.area(), 10)

        # pass an argument in the area function
        with self.assertRaises(TypeError):
            k.area(10, 10)

        # pass none as argument
        with self.assertRaises(TypeError):
            k.area(None)

    def test_display(self):
        '''test the display method'''
        # test the avialbility of the method
        self.assertTrue('display' in dir(Rectangle))

        g = Rectangle(2, 2, 2, 2, 2)
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

    def test__str_method(self):
        '''testing the str method'''
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')

        # check when a function is passed few arguments
        r2 = Rectangle(5, 5, 1, 1, 10)
        self.assertEqual(r2.__str__(), '[Rectangle] (10) 1/1 - 5/5')

        with self.assertRaises(TypeError):
            r1.__str__(1)


class TestRectangle_update_args(unittest.TestCase):
    '''testing the args update'''

    def test_update_args(self):
        '''testing updates with no-keyword argument/positional arguments'''
        p = Rectangle(10, 10, 10, 10)

        # passing one arguments
        p.update(89)
        self.assertEqual(p.id, 89)
        self.assertEqual(p.width, 10)
        self.assertEqual(p.height, 10)
        self.assertEqual(p.x, 10)

        # pass 2 arguments
        p.update(7, 8)
        self.assertEqual(p.id, 7)
        self.assertEqual(p.width, 8)
        self.assertEqual(p.height, 10)
        self.assertEqual(p.x, 10)
        self.assertEqual(p.y, 10)

        # passsing 3 arguments
        p.update(89, 2, 3)
        self.assertEqual(p.__str__(), '[Rectangle] (89) 10/10 - 2/3')

        # passing 4 arguments
        p.update(89, 2, 3, 4)
        self.assertEqual(p.__str__(), '[Rectangle] (89) 4/10 - 2/3')

        # passing 5 arguments
        p.update(89, 2, 3, 4, 5)
        self.assertEqual(p.__str__(), '[Rectangle] (89) 4/5 - 2/3')

        # passing more that 5 args
        p.update(89, 2, 3, 4, 5, 9)
        self.assertEqual(p.__str__(), '[Rectangle] (89) 4/5 - 2/3')

    def test_nonint_args(self):
        ''' tesing args update function with non ints'''
        # passing none int value
        p = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            p.update(89, 'bs', 3, 4, 5)

        # passing non int height
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            p.update(89, 9, 'bs', 3, 5)

        # passing non int x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            p.update(8, 89, 90, 'bopm', 5)

        # passing non int y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            p.update(89, 90, 5, 8, 4.989787)

    def test_negative_args(self):
        '''in the update function testing with negative values'''
        p = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            p.update(89, -8, 3, 4, 5)

        # passing negative value in height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            p.update(89, 8, -3, 4, 5)

        # passing x as negative
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            p.update(89, 8, 3, -4, 5)

        # passing x as negative
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            p.update(89, 8, 3, 4, -5)

    def test_zero_args(self):
        '''testing when you pass zero an argument in the update function'''
        p = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            p.update(89, 0, 3, 4, 5)

        # passing 0 value in height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            p.update(89, 8, 0, 4, 5)

        # passing zero in x
        p.update(89, 8, 5, 0)
        self.assertEqual(0, p.x)

        p.update(89, 8, 5, 0, 0)
        self.assertEqual(0, p.y)

    def test_nothing_passed(self):
        '''passing nothing to update function'''
        # passing Nothing
        p = Rectangle(10, 10, 10, 10, 10)
        p.update()
        self.assertEqual(str(p), '[Rectangle] (10) 10/10 - 10/10')


class TestRectangle_update_kwargs(unittest.TestCase):
    '''testing the update for kwargs'''

    def test_update_kwargs(self):
        '''test the update function with kwargs and args combined'''
        r = Rectangle(10, 10, 10, 10, 2)

        # empty update
        r.update()
        self.assertEqual(r.__str__(), '[Rectangle] (2) 10/10 - 10/10')

        # test ints for kwargs
        r.update(x=1, height=2, y=3, width=4, id=89)
        self.assertEqual(r.__str__(), '[Rectangle] (89) 1/3 - 4/2')

        # pass if extra args in kwargs
        r.update(x=1, height=2, y=3, width=4, id=89, bion=45)
        self.assertEqual(r.__str__(), '[Rectangle] (89) 1/3 - 4/2')

    def test_args_and_kwarg(self):
        ''' test when args and kwargs passed together'''

        p = Rectangle(10, 10, 10, 10)
        p.update(90, height=1)
        self.assertEqual(p.__str__(), '[Rectangle] (90) 10/10 - 10/10')

    def test_kwargs_nonints(self):
        ''' testing non ints when passed'''

        # passing none int value
        p = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            p.update(width='bs')

        # passing non int height
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            p.update(height=78.09)

        # passing non int x
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            p.update(x='bopm')

        # passing non int y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            p.update(y=4.989787)

    def test_negative_kwars(self):
        '''passing negativa value in kwargs'''
        p = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            p.update(width=-8)

        # passing negative value in height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            p.update(height=-3)

        # passing x as negative
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            p.update(x=-4)

        # passing x as negative
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            p.update(y=-5)

    def test_zero_kwargs(self):
        '''passing zero for kwargs values'''
        p = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            p.update(width=0)

        # passing 0 value in height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            p.update(height=0)

        # passing zero in x
        p.update(x=0)
        self.assertEqual(0, p.x)

        p.update(y=0)
        self.assertEqual(0, p.y)


class Test_to_dictionary(unittest.TestCase):
    '''test the method to dictionary'''
    def test_to_dict(self):
        ''' test the to dic method'''
        r1 = Rectangle(10, 2, 1, 9, 1)
        r2 = r1.to_dictionary()
        self.assertEqual(
                r2,
                {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertEqual(dict, type(r2))
