#!/usr/bin/python3
'''defines classs student'''


class Student:
    '''this is the class student'''
    def __init__(self, first_name, last_name, age):
        '''intialise arguments as public attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            newlist = []
            for x in attrs:
                if x == 'first_name':
                    tup = (x, self.first_name)
                    newlist.append(tup)
                if x == 'last_name':
                    tup = (x, self.last_name)
                    newlist.append(tup)
                if x == 'age':
                    tup = (x, self.age)
                    newlist.append(tup)
            return dict(newlist)
        '''converts the class to json format'''
        return self.__dict__
