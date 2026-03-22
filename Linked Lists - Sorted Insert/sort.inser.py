def sorted_insert(head, data):
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
            head.next =temp
            break

        head = head.next
    return start
