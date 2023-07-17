#!/usr/bin/python3
'''Testing base classs in th module base'''
import unittest
import os
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
from os.path import exists


class TestBase(unittest.TestCase):
    '''test the class base using inittest'''
    def test_class(self):
        '''test the existance of class an its attributes'''
        # test the class without creating an object
        self.assertTrue(issubclass(Base, object))
        self.assertFalse(issubclass(Base, int))

    def test_attributes(self):
        '''test attributes'''
        b = Base()
        self.assertEqual(b._Base__nb_objects, 1)
        self.assertEqual(b.id, 1)
        self.assertTrue('__init__' in dir(b))

    def test_id_not_none(self):
        # test when the id is not none
        b1 = Base(23)
        self.assertEqual(b1.id, 23)
        self.assertEqual(b1._Base__nb_objects, 1)


class Test_to_json(unittest.TestCase):
    '''test to json method'''

    def test_to_json_string(self):
        ''' test to_json method '''
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        jsn = Base.to_json_string([dictionary])
        self.assertEqual(type(jsn), str)
        self.assertEqual(
                jsn,
                '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]')

        self.assertEqual(Base.to_json_string([23, 34, 1]), '[23, 34, 1]')

    def test_to_json_empty(self):
        '''test when passed an empty dictionary'''
        r1 = Rectangle(10, 7, 2, 8, 1)
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_none(self):
        '''test none in to json'''
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_non_list(self):
        '''passing non list item'''
        self.assertEqual(Base.to_json_string(34), '34')
        self.assertEqual(Base.to_json_string('bion'), '"bion"')

    def test_to_json_tuple(self):
        r = ((1, 1), (2, 4))
        self.assertEqual('[[1, 1], [2, 4]]', Base.to_json_string(r))


class Testsave_to_file(unittest.TestCase):
    ''' tasting the method save_to_file'''

    def test_file(self):
        ''' test if it creates file'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(exists("Rectangle.json"))
        self.assertNotEqual(os.stat('Rectangle.json').st_size, 0)

    def test_none(self):
        Rectangle.save_to_file(None)
        self.assertTrue(exists("Rectangle.json"))
        self.assertNotEqual(os.stat('Rectangle.json').st_size, 0)

    def test_read_file(self):
        Rectangle.save_to_file(None)
        '''read the json file'''
        with open("Rectangle.json", "r") as mfile:
            self.assertEqual('[]', mfile.read())

        r2 = Rectangle(2, 4, 0, 0, 5)
        Rectangle.save_to_file([r2])
        with open("Rectangle.json", "r") as mfile:
            self.assertEqual(
                    '[{"id": 5, "width": 2, "height": 4, "x": 0, "y": 0}]',
                    mfile.read())

    def test_non_iterables(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(1)

    def test_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(1, 6, 2, 2)


class Testfrom_json_string(unittest.TestCase):
    '''test  from_json_string method'''
    def test_None(self):
        ''' test when None passed'''
        self.assertEqual(Rectangle.to_json_string(None), '[]')

    def test_empty(self):
        '''test when Nothing is passed'''
        with self.assertRaises(TypeError):
            Rectangle.to_json_string()

    def test_non_json(self):
        '''non json string passed'''
        k = Rectangle.to_json_string('boin')
        self.assertEqual(k, '"boin"')

    def test_dict(self):
        '''test with a list of dict'''
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        out = Rectangle.from_json_string(json_list_input)

        self.assertEqual(out, [{'id': 89, 'width': 10, 'height': 4}])


class Testcreate(unittest.TestCase):
    '''test the create function '''

    def test_kwargs(self):
        '''pass kwargs full'''
        r1 = Rectangle(3, 5, 1, 0, 1)
        r2 = r1.to_dictionary()
        r3 = Rectangle.create(**r2)
        self.assertEqual(str(r3), '[Rectangle] (1) 1/0 - 3/5')
        self.assertTrue(isinstance(r3, Rectangle))

    def test_few_kwargs(self):
        ''' pass it lest than full'''
        r3 = Rectangle.create(width=3, height=4, id=1)
        self.assertEqual(str(r3), '[Rectangle] (1) 0/0 - 3/4')

    def test_with_args(self):
        ''' pass args insted of kwargs'''
        with self.assertRaises(TypeError):
            r3 = Rectangle.create(4, 5, 2, 1)

    def test_with_none(self):
        ''' pass it none as paremeter'''
        with self.assertRaises(TypeError):
            r3 = Rectangle.create(None)

    def test_with_list(self):
        with self.assertRaises(TypeError):
            r3 = Rectangle.create([1, 2, 3, 4])

    def test_empty(self):
        '''test when nothing is passsed'''
        r3 = Rectangle.create()
        self.assertEqual(str(r3), 'None')


class Testload_from_file(unittest.TestCase):
    '''testing the load_from_file method'''

    def test_with_file(self):
        ''' test when the file exits'''
        s1 = Square(5, 0, 0, 5)
        list_squares_input = [s1]

        Square.save_to_file(list_squares_input)
        output = Square.load_from_file()
        for square in output:
            self.assertEqual(str(square), '[Square] (5) 0/0 - 5')

    def test_arg_passed(self):
        ''' test when passed arguments in function '''
        with self.assertRaises(TypeError):
            output = Square.load_from_file(1, 2)

    def test_with_None(self):
        ''' test when nothing is passed '''
        with self.assertRaises(TypeError):
            output = Square.load_from_file(None)
