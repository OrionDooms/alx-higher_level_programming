#!/usr/bin/python3

"""A Node class"""


class Node:
    """Node cilass defined"""
    def __init__(self, data, next_node=None):
        """initialize the assigned values to object property

        Args:
            data: the data of the linked list.
            next_node: the next_node of the linked list"""
        self.data = data
        self.next = next_node

    def data(self):
        """The data() method, get or set the current data."""
        self.__data

    def data(self, value):
        """data must be an integer"""
        if type(data) != int:
            raise TypeError("data must be an integer")

    def next_node(self):
        self.__next_mode

    def next_node(self, value):
        """next_node can be None or must be a Node"""
        if (next_node is not None) or (next_node is not Node):
            raise TypeError("next_node must be a Node object")


"""A SinglyLinkedList class"""


class SinglyLinkedList:
    """SinglyLinkedList class defined"""
    def __init__(self):
        """initialize the assigned values to object property"""
    def sorted_insert(self, value):
        """sorted position in the list (increasing order)"""
        print(value)
