# coding=utf-8
"""
shu
"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums + 1]) if values[nums + 1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1

    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret


def mirror_bfs(root):
    ret = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            ret.append(node.val)
            queue.append(node.right)
            queue.append(node.left)
            print("change {}".format(node.right))
    return ret


if __name__ == '__main__':
    t1 = Tree()
    t1.construct_tree([1, 2, 3, 4, 5])
    t2 = Tree()
    t2.construct_tree([2])
    print(mirror_bfs(t1.root))
