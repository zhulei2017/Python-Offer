
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def last_kth(link, k):
    if not link or k <= 0:
        return None
    move = link
    while move and k-1 >= 0:
        move = move.next
        k -= 1
    while move:
        move = move.next
        link = link.next
    if k == 0:
        return link.val
    return None


def gen_link(length):
    node1 = ListNode(0)
    link = node1
    for i in range(1, length):
        node = ListNode(i)
        link.next = node
        link = link.next
    return node1


if __name__ == "__main__":
    node_test = gen_link(5)
    print(last_kth(node_test, 4))
