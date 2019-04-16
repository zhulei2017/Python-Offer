class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Link:

    @staticmethod
    def link(values):
        head = ListNode(0)
        move = head
        try:
            for val in values:
                tmp = ListNode(val)  # <__main__.ListNode object at 0x033F8A70>
                move.next = tmp
                move = move.next
        except Exception as e:
            print(e)
        return head.next


# using stack
def print_links_back(links):
    stack = []
    ans = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        ans.append(stack.pop())
        #print(stack.pop())
    return ans


#using recursion
def print_links_back_rec(links):
    if links is not None:
        print_links_back_rec(links.next)
        print(links.val)


if __name__ == "__main__":
    links = Link.link([1, 2, 3, 4, 5, 6])
    print(print_links_back(links))
    # print_links_back_rec(links)


