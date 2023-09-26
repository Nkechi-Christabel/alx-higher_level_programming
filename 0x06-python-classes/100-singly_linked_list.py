#!/usr/bin/python3

"""A class Node that defines a node of a singly linked list by"""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        _data (int): The integer data stored in the node.
        _next_node (Node): The next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node with the given data and optional next node.

        Args:
            data (int): The integer data to store in the node.
            next_node (Node, optional): The next node in the linked list.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Gets the data stored in the node.

        Returns:
            int: The integer data stored in the node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The new integer data to store in the node.

        Raises:
            TypeError: If the new data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Gets the next node in the linked list.

        Returns:
            Node: The next node in the linked list, or None if there is no
            next node.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The new next node in the linked list, or None.

        Raises:
            TypeError: If the new next node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head node of the linked list.
    """
    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node with the given value into the correct sorted
        position in the list.

        Args:
            value (int): The integer value to insert into the list.

        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value <= self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the singly linked list.

        Returns:
            str: A string containing one node's data per line.
        """
        result = []
        current = self.head

        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
