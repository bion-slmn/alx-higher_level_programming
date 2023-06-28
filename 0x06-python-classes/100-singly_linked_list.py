#!/usr/bin/python3
'''defines node of s singly list'''


class Node:
    '''blue print for node in a singly list'''

    def __init__(self, data, next_node=None):
        '''intialise a node

        Args:
            data (int): is an integer
            next_node (node): address of next node'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''return the private data'''
        return self.__data

    @data.setter
    def data(self, value):
        '''set the data'''
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    '''represent a singly list'''

    def __init__(self):
        '''intialize the head of the list'''
        self.__head = None

    def sorted_insert(self, value):
        '''insert the a value in a sorted list'''
        if self.__head is None or self.__head.data >= value:
            newNode = Node(value, self.__head)
            self.__head = newNode

        else:
            temp = self.__head
            while temp.next_node and temp.next_node.data < value:
                temp = temp.next_node

            newNode = Node(value, temp.next_node)
            temp.next_node = newNode

    def __str__(self):
        if self.__head is None:
            print()
        else:
            temp = self.__head
            result = []
            while temp:
                result.append(str(temp.data))
                temp = temp.next_node

        return "\n".join(result)
