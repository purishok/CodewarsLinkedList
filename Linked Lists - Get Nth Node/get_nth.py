"""
Module for indexing and retrieving elements from a singly linked list.

This module provides a robust way to access nodes by their position,
including validation for empty lists and out-of-bounds indices.
"""

from preloaded import Node

def get_nth(node, index):
    """
    Retrieve the node at a specific index in a linked list.

    The function first calculates the total length of the list to validate
    the index, then traverses the list again to find the target node.

    Args:
        node: The head node of the linked list.
        index (int): The zero-based index of the node to retrieve.

    Returns:
        Node: The node object located at the specified index.

    Raises:
        Exception: If the list is empty, the index is negative,
                  or the index exceeds the length of the list.
    """
    if not node:
        raise Exception("Cannot get element from an empty list.")

    num = -1
    probe = node
    while probe is not None:
        num += 1
        probe = probe.next

    if index < 0 or index > num:
        raise Exception(f"Index {index} is out of bounds.")

    num = 0
    result = node
    while num != index:
        result = result.next
        num += 1

    return result
