#!/usr/bin/python3
'''defines classs student'''


class Student:
    '''this is the class student'''
    def __init__(self, first_name, last_name, age):
        '''intialise arguments as public attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''converts the class to json format'''
        return self.__dict__
