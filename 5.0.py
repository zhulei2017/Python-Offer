class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


llist1 = LNode(1)
p = llist1
for i in range(2, 11):
    p.next = LNode(i)
    p = p.next

p = llist1
while p is not None:
    print(p.elem)
    p = p.next


class LinkedListUnderflow(ValueError):
    pass


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e


# head = LNode(0)
# q = LNode(13)
# q.next = head.next
# head = q
# p = LNode(14)
# p.next = q.next
# q.next = p
#
# print(q.next.elem)
