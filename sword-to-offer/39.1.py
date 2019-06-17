from collections import deque


def get_depth(treeroot):
    if not treeroot:    # 不是结点
        return 0
    if not treeroot.left and not treeroot.right:    # 同时没有左右子树
        return 1
    return 1 + max(get_depth(treeroot.left), get_depth(treeroot.right))


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
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


if __name__ == "__main__":
    t = Tree()
    t.construct_tree([1, 2, 3, 4])
    print(t.bfs())
    print(get_depth(t.root))
