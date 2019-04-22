import random


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.other = None


class Solution:

    @staticmethod
    def clone_nodes(head):
        move = head
        while move:
            tmp = Node(move.val)
            tmp.next = move.next
            move.next = tmp
            move = tmp.next  # 保存下一链表结点，进入下一轮循环
        return head

    @staticmethod
    def set_nodes(head):
        move = head
        while move:
            m_next = move.next
            if move.other:
                m_next.other = move.other.next
            move = m_next.next
        return head

    @staticmethod
    def reconstruct_nodes(head):
        ret = head.next if head else Node
        move = ret
        while head:
            head = move.next
            if head:
                move.next = head.next
                move = move.next
        return ret

    @staticmethod
    def clone_link(head):
        h = Solution.clone_nodes(head)
        h = Solution.set_nodes(h)
        ret = Solution.reconstruct_nodes(h)
        return ret

    @staticmethod
    def print_nodes(head):
        ret = []
        while head:
            tmp = [head.val]
            if head.other:
                tmp.append(head.other.val)
            ret.append(tmp)
            head = head.next
        print(ret)

    @staticmethod
    def construct_nodes(vals):
        if not vals:
            return Node
        move = head = Node(vals.pop(0))
        nodes = [None, head]
        for v in vals:
            tmp = Node(v)
            move.next = tmp
            nodes.append(tmp)
            move = move.next
        move = head
        while move:
            move.other = random.choice(nodes)
            move = move.next
        return head


if __name__ == '__main__':
    link = Solution.construct_nodes([1, 2, 3, 4, 5])
    Solution.print_nodes(link)
    test = Solution.clone_link(link)
    Solution.print_nodes(test)
