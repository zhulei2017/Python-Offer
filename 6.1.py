class TreeNode:
    """
    二叉树结点定义
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinTree:
    def __init__(self):
        self.root = None

    def bfs(self):




def reconstr(pre, tin):
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])

    index = tin.index(pre[0])
    left = tin[0:index]
    right = tin[index+1:]
    root = TreeNode(pre[0])
    root.left = reconstr(pre[1: 1+len(left)], left)
    root.right = reconstr(pre[len(left)+2:], right)
    return root


if __name__ == "__main__":
    root1 = reconstr([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    print()
