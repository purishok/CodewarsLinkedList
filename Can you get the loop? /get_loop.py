"""
Module for detecting and measuring loops in singly linked lists.

This module provides utility functions to analyze the structure of linked lists,
specifically focusing on identifying the size of cyclic patterns.
"""

def loop_size(node):
    """
    Calculate the number of nodes in a linked list loop.

    Uses Floyd's Cycle-Finding Algorithm to detect the cycle and then
    traverses the loop to determine its exact length.

    Args:
        node: The head node of the linked list. Each node is expected
              to have a 'next' attribute.

    Returns:
        int: The number of nodes within the loop.
    """
    probe_1, probe_2 = node.next, node.next.next
    while probe_1 != probe_2:
        probe_1 = probe_1.next
        probe_2 = probe_2.next.next

    count = 1
    probe_2 = probe_2.next
    while probe_1 != probe_2:
        count += 1
        probe_2 = probe_2.next

    return count
