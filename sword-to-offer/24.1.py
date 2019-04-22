def is_post_order(order):
    length = len(order)
    if length:
        root = order[-1]
        left = 0
        while order[left] < root:
            left += 1
        right = left
        while right < length - 1:
            if order[right] < root:
                return False
            right += 1
        left_ret = True if left == 0 else is_post_order(order[: left])
        right_ret = True if right == 0 else is_post_order(order[left: right])
        return left_ret and right_ret
    return False


if __name__ == "__main__":
    print(is_post_order([5, 7, 6, 9, 11, 10, 8]))
