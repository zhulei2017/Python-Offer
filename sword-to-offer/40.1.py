def get_only_one_number(nums):
    if not nums:
        return None
    tmp_ret = 0
    for n in nums:    # 获取两个值的异或结果，^ 异或符号
        tmp_ret ^= n
    last_one = get_bin(tmp_ret)
    a_ret, b_ret = 0, 0
    for n in nums:
        if is_one(n, last_one):
            a_ret ^= n
        else:
            b_ret ^= n
    return [a_ret, b_ret]


def get_bin(num):
    ret = 0
    while num & 1 == 0 and ret < 32:
        num = num >> 1
        ret += 1
    return ret


def is_one(num, t):    # 验证t位是不是1
    num = num >> t
    return num & 0x01


if __name__ == "__main__":
    test = [2, 4, 3, 6, 3, 2, 5, 5]
    print(get_only_one_number(test))
