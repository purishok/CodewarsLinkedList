"""
Module for linked list construction utilities.

Provides functions to prepend data to an existing list and a helper
to build a standard three-node list (1 -> 2 -> 3).
"""

from preloaded import Node

def push(head, data):
    """
    Insert a new node with the given data at the beginning of a linked list.

    Args:
        head: The current head node of the list (can be None).
        data: The data to be stored in the new node.

    Returns:
        Node: The new head of the list, which points to the old head.
    """
    n = Node(data)
    n.next = head
    return n

def build_one_two_three():
    """
    Create a linked list representing the sequence [1, 2, 3].

    This is a convenience function often used for testing linked list
    algorithms. It builds the list in reverse order (3, then 2, then 1)
    using the push function to ensure the final head points to 1.

    Returns:
        Node: The head of the list (node with data 1).
    """
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)
    return head
