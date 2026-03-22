"""
Module for linked list visualization and string representation.

This module provides tools to convert custom linked list structures
into human-readable string formats.
"""

def stringify(node):
    """
    Convert a linked list into a string representation.

    Traverses the linked list starting from the given node and formats
    the data of each node into a visual chain ending with 'None'.

    Args:
        node: The head node of the linked list. Expected to have
              'data' and 'next' attributes.

    Returns:
        str: A string in the format "data1 -> data2 -> ... -> None".
             Returns 'None' if the input node is None.
    """
    result = ''
    while node:
        result += str(node.data) + ' -> '
        node = node.next
    return result + 'None'
