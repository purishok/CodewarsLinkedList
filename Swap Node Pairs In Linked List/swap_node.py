from preloaded import Node

def swap_pairs(head):
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
