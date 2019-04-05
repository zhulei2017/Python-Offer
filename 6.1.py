from collections import deque


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

    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return 0
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)

        traversal(self.root)
        return ret

    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return 0
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return 0
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret


def reconstr(pre, tin):
    if len(pre) == 0:
        return None
    if len(tin) == 0:
        return None
    # if len(pre) == 1:  #当只有一个值时，可以接着迭代，为0时终止，所以可以不是终止条件
    #     return TreeNode(pre[0])

    index = tin.index(pre[0])
    left = tin[0:index]
    right = tin[index+1:]
    root = TreeNode(pre[0])
    root.left = reconstr(pre[1: 1+len(left)], left)
    root.right = reconstr(pre[-len(right):], right)
    return root


if __name__ == "__main__":
    t = BinTree()
    root1 = reconstr([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    t.root = root1
    print("the pre traversal is {}".format(t.pre_traversal()))
    print("the mid traversal is {}".format(t.in_traversal()))
    print("the post traversal is {}".format(t.post_traversal()))
