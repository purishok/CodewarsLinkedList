"""
Module for linked list reversal operations.

This module provides structures and methods to invert the direction
of nodes in a singly linked list.
"""

class Node(object):
    """Represents a single node in a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """
    Reverse a linked list using a recursive approach.

    This function traverses to the end of the list and then re-links
    each node to its predecessor as the recursion unwinds.

    Args:
        head: The head node of the list to be reversed.

    Returns:
        Node: The new head of the reversed list (formerly the last node).
              Returns the original head if the list is empty or has one node.
    """
    if head is None or head.next is None:
        return head

    new_head = reverse(head.next)

    head.next.next = head

    head.next = None

    return new_head
