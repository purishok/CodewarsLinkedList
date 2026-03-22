from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    res = list_repr.split(' -> ')
    result = Node(0)
    start = result
    for el in res[:-1]:
        result.next = Node(int(el))
        result = result.next
    return start.next
