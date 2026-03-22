"""
Module for manipulating linked list structures through splitting operations.

This module provides classes for node representation and context storage,
along with functions to redistribute nodes between multiple lists.
"""

class Node(object):
    """Represents a single node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    """A container to hold two linked lists resulting from a split."""
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Split a linked list into two separate lists by alternating nodes.

    The first node goes to the 'first' list, the second to the 'second' list,
    the third to the 'first', and so on.

    Args:
        head: The head node of the source linked list.

    Returns:
        Context: An object containing the heads of the two new lists.

    Raises:
        Exception: If the source list is empty or has only one node.
    """
    if head is None or head.next is None:
        raise Exception("List must have at least two nodes to perform an alternating split.")
    probe_1 = Node()
    probe_2 = Node()
    end_1 = probe_1
    end_2 = probe_2

    current = head
    while current is not None:
        end_1.next = current
        end_1 = end_1.next
        current = current.next

        if current is not None:
            end_2.next = current
            end_2 = end_2.next
            current = current.next

    end_1.next = None
    end_2.next = None

    return Context(probe_1.next, probe_2.next)
