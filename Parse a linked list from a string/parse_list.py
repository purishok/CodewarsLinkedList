"""
Module for reconstructing linked lists from string representations.

This module provides a parser that converts serialized linked list strings
back into functional Node-based data structures.
"""

from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    """
    Parse a string representation of a linked list back into a Node structure.

    The string is expected to be in the format "val1 -> val2 -> ... -> None".
    The function splits the string and iterates through the values to
    reconstruct the list.

    Args:
        list_repr (str): The string representation of the list (e.g., "1 -> 2 -> None").

    Returns:
        Node | None: The head of the reconstructed linked list,
                     or None if the list string represents an empty list.
    """
    res = list_repr.split(' -> ')
    result = Node(0)
    start = result
    for el in res[:-1]:
        result.next = Node(int(el))
        result = result.next

    return start.next
