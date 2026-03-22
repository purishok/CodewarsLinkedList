from preloaded import Node

def get_nth(node, index):
    if not node:
        raise Exception()

    num = -1
    probe = node
    while probe is not None:
        num+=1
        probe = probe.next

    if index<0 or index>num:
        raise Exception()

    num = 0
    result = node
    while num!=index:
        result = result.next
        num+=1
    return result
