from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    """
    非二叉搜索树
    """
    def __init__(self):
        self.root = None

    def construct_tree(self, values = None):
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


class Solution:

    @staticmethod
    def convert(tree):
        if not tree:
            return None
        p_last = Solution.convert_node(tree, None)
        while p_last and p_last.left:   # 获取链表头结点
            p_last = p_last.left
        return p_last

    @staticmethod
    def convert_node(tree, last):
        """
        why?
        :param tree:
        :param last:
        :return:
        """
        if not tree:
            return None
        if tree.left:
            last = Solution.convert_node(tree.left, last)
        if last:
            last.right = tree
        tree.left = last
        last = tree
        if tree.right:
            last = Solution.convert_node(tree.right, last)
        return last

    @staticmethod
    def print_nodes(tree):
        ret = []
        while tree:
            tmp = []
            tmp.append(tree.left.val if tree.left else None)
            tmp.append(tree.val)
            tmp.append(tree.right.val if tree.right else None)
            ret.append(tmp)
            tree = tree.right
        print(ret)


if __name__ == '__main__':
    r = Tree()
    r.construct_tree([10, 6, 14, 4, 8, 12, 16])
    print(r.bfs())
    t = Solution.convert(r.root)
    Solution.print_nodes(t)

