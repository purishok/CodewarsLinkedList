"""
Module for ordered data insertion in linked lists.

Provides functionality to insert new nodes into a pre-sorted
singly linked list while maintaining the ascending order.
"""

def sorted_insert(head, data):
    """
    Insert a new node with the given data into a sorted linked list.

    The function maintains ascending order by identifying the correct
    position for the new data. It handles three main cases:
    1. Empty list (new node becomes the head).
    2. Data is smaller than the current head (new node becomes the new head).
    3. Data belongs somewhere in the middle or at the end.

    Args:
        head: The head node of a sorted linked list (can be None).
        data: The value to be inserted.

    Returns:
        Node: The head of the updated sorted linked list.
    """
    if head is None:
        return Node(data)

    start = head

    if head.data > data:
        temp = Node(data)
        temp.next = head
        start = temp
        return start

    while head is not None:
        if head.next == None or head.next.data > data:
            temp = Node(data)
            temp.next = head.next
            head.next = temp
            break

        head = head.next

    return start
