#!/usr/bin/python3
'''The class inherits list'''


class MyList(list):
    '''Mylist inherits from list class

    Args:
        list(obj): is parent class of Mylist
    '''
    def print_sorted(self):
        '''prints the lists in asscending order

        Args:
            self(obj): the oblect itself
        '''
        print("{}".format(sorted(self)))
