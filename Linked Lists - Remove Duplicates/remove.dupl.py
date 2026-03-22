"""
Module for removing duplicate elements from linked list structures.

Provides methods to ensure that each data value appears only once
in a sorted sequence of nodes.
"""

class Node(object):
    """Represents a single node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Remove duplicate nodes from a sorted linked list.

    Iterates through the list once and skips over any nodes that
    contain the same data as the current node.

    Args:
        head: The head node of a sorted linked list.

    Returns:
        Node: The head of the list with all duplicate values removed.
              Returns None if the input list is empty.
    """
    if head is None:
        return None

    current = head
    while current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head
