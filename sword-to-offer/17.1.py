# coding = utf-8
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


# 递归，终止条件是
def merge_link(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    if head1.val <= head2.val:
        ret = head1
        ret.next = merge_link(head1.next, head2)
    else:
        ret = head2
        ret.next = merge_link(head1, head2.next)
    return ret


class Nodes:
    def __init__(self, values=None):
        self.nodes = self._set_link(values) if values else None

    def get_link(self):
        return self.nodes

    def print_self(self):
        Nodes.print_link(self.nodes)

    @staticmethod
    def print_link(link=None):
        count = 1
        while link:
            if count == 1:
                print(link.val)
            elif count % 5 == 0:
                print("->{}".format(link.val))
            else:
                print("->{}".format(link.val))
            count += 1
            link = link.next

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


if __name__ == "__main__":
    nodes = Nodes([1, 3, 5])
    h1 = nodes.get_link()
    nodes2 = Nodes([2, 4, 6])
    h2 = nodes2.get_link()
    ret = merge_link(h1, h2)
    Nodes.print_link(ret)