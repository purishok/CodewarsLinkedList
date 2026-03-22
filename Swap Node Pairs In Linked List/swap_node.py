"""
Module for reordering linked lists by swapping adjacent nodes.

This module provides an efficient way to swap pairs of nodes
without modifying the data within the nodes, only their pointers.
"""

from preloaded import Node

def swap_pairs(head):
    """
    Swap every two adjacent nodes in a linked list and return its head.

    The function re-links the nodes in pairs (1st with 2nd, 3rd with 4th, etc.).
    If the list has an odd number of nodes, the last node remains in place.

    Args:
        head: The head node of the linked list.

    Returns:
        Node: The new head of the list after pairwise swapping.
              Returns the original head if the list has fewer than two nodes.
    """
    if head is None or head.next is None:
        return head
    probe_1 = Node()
    probe_1.next = head
    prev = probe_1
    while prev.next is not None and prev.next.next is not None:
        a = prev.next
        b = prev.next.next
        prev.next = b
        a.next = b.next
        b.next = a
        prev = a

    return probe_1.next
