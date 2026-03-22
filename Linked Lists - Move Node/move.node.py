"""
Module for node migration between linked lists.

Contains utility classes and functions to transfer nodes from a source
linked list to a destination linked list.
"""

class Node(object):
    """Represents a single node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    """
    A container that holds the state of two lists after a node transfer.

    Attributes:
        source: The remaining part of the original source list.
        dest: The new destination list with the transferred node at the front.
    """
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Move the front node from the source list to the front of the destination list.

    This function effectively 'pops' the head of the source list and
    'pushes' it onto the destination list.

    Args:
        source: The head node of the list to move a node from.
        dest: The head node of the list to move a node to (can be None).

    Returns:
        Context: An object containing the new heads of both lists.

    Raises:
        AttributeError: If source is None (cannot move a node from an empty list).
    """
    new_source = source.next

    new_dest = Node(source.data)
    new_dest.next = dest

    return Context(new_source, new_dest)
