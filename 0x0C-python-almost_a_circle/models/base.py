#!/usr/bin/python3
'''This module creates a class called Base'''
import json
import csv
import os.path


class Base:
    '''base has class varible and instance variable'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''class constructor'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' convert the list_dictionary to json string'''
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)

        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        ''' save json  string to json file'''
        filename = cls.__name__

        if list_objs is None:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]

        with open(filename + ".json", 'w', encoding='utf-8') as myfile:
            myfile.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        ''' return a list from json string'''
        if json_string:
            return json.loads(json_string)

        return []

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set'''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        else:
            with open(filename, encoding='utf-8') as f:
                content = f.read()
                new_list_dict = cls.from_json_string(content)

                list_obj = [cls.create(**obj) for obj in new_list_dict]

            return list_obj

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' saving to csv file'''
        filename = cls.__name__ + '.csv'

        if filename == 'Rectangle.csv':
            header = ['id', 'width', 'height', 'x', 'y']
        else:
            header = ['id', 'size', 'x', 'y']

        if list_objs is None:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]

        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
                return
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        '''loading from csv file'''
        filename = cls.__name__ + '.csv'
        if not os.path.exists(filename):
            return []

        with open(filename, encoding='utf-8') as f:
            if filename == 'Rectangle.csv':
                header = ['id', 'width', 'height', 'x', 'y']
            else:
                header = ['id', 'size', 'x', 'y']

            c_file = csv.DictReader(f, fieldnames=header)
            content = [dict([k, int(v)] for k, v in d.items()) for d in c_file]
            list_obj = [cls.create(**obj) for obj in content]

        return list_obj
