class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Nodes:
    def __init__(self, values=None):
        self.nodes = self._set_link(values) if values else None

    def get_link(self):
        return self.nodes

    def get_tail(self):
        tail = self.nodes
        while tail.next:
            tail = tail.next
        return tail

    def print_self(self):
        Nodes.print_link(self.nodes)

    @staticmethod
    def print_link(link=None):
        count = 1
        while link:
            if count == 1:
                print(link.val)
            elif count % 5 == 0:
                print('->', link.val)
            else:
                print('->', link.val, ',')
            count += 1
            link = link.next
        print()

    def _set_link(self, values):
        head = ListNode(0)
        move = head
        try:
            for val in values:
                tmp = ListNode(val)
                move.next = tmp
                move = move.next
        except Exception as e:
            print(e)
        return head.next


def get_first_common_node(link1, link2):
    if not link1 or not link2:
        return None
    length1, length2 = 0, 0
    move1, move2 = link1, link2
    while move1.next:
        length1 += 1
        move1 = move1.next
    while move2.next:
        length2 += 1
        move2 = move2.next
    while length1 > length2:
        length1 -= 1
        link1 = link1.next
    while length2 > length1:
        length2 -= 1
        link2 = link2.next
    while link1:
        if link1 == link2:
            return link1
        link1, link2 = link1.next, link2.next
    return None


if __name__ == '__main__':
    t1 = [1, 2, 3, 4]
    t2 = [5, 6, 7, 8, 12]
    t3 = [9, 10, 11]
    node1, node2, common = Nodes(t1), Nodes(t2), Nodes(t3)
    h1 = node1.get_link()
    h2 = node2.get_link()
    h3 = common.get_link()
    tail1 = node1.get_tail()
    tail2 = node2.get_tail()
    tail1.next = h3
    tail2.next = h3
    print(get_first_common_node(h1, h2).val)


