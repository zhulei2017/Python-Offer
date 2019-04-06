class ListNode:
    def __init__(self, num):
        self.val = num
        self.next = None


def delete_node(link, node):
    if link == node:
        del node
        return print("NuLL")
    if node.next == None:
        while link.next:
            if link.next == node:
                link.next == None
            link = link.next
    else:
        node.val = node.next.val
        node.next = node.next.next


if __name__ == "__main__":
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(3)
    node2 = ListNode(11)
    delete_node(node1, node1.next)
    delete_node(node2, node2)
    print(node1.val)
    print(node1.next.val)
    print(node2.val)

