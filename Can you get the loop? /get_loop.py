def loop_size(node):
    probe_1, probe_2 = node.next, node.next.next
    while probe_1 != probe_2:
        probe_1 = probe_1.next
        probe_2 = probe_2.next.next
    count = 1
    probe_2 = probe_2.next
    while probe_1 != probe_2:
        count += 1
        probe_2 = probe_2.next

    return count
