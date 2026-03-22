from preloaded import Node

def push(head, data):
    n = Node(data)
    n.next = head
    return n

def build_one_two_three():
    head = None
    for i in range(3,0,-1):
        head = push(head,i)
    return head
