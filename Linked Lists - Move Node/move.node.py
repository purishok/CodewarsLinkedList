class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    new_source = source.next
    new_dest = Node(source.data)
    new_dest.next = dest
    return Context(new_source, new_dest)
