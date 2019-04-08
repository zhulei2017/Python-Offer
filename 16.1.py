# coding=utf-8
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# def reverse_link(head):
#     if not head or not head.next:
#         return head
#     then = head.next
#     head.next = None
#     last = then.next
#     while then:
#         then.next = head
#         head = then
#         then = last
#         if then:
#             last = then.next
#     return head


def reverse_link(head):
    if not head or not head.next:
        return head
    pnode = head
    pprev = None
    while pnode:
        pnext = pnode.next
        if pnext == None:
            preversedhead = pnode
        pnode.next = pprev
        pprev = pnode   # pnode 是下一个循环里的pprev
        pnode = pnext   # pnext保存后赋给pnode，进入下一循环
    return preversedhead


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
    test = reverse_link(node_test)
    print(test.val)
