class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception()

    probe_1 = Node()
    probe_2 = Node()
    end_1 = probe_1
    end_2 = probe_2

    current = head
    while current is not None:
        end_1.next = current
        end_1 = end_1.next
        current = current.next

        if current is not None:
            end_2.next = current
            end_2 = end_2.next
            current = current.next

    end_1.next = None
    end_2.next = None

    return Context(probe_1.next, probe_2.next)
