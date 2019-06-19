import random


def is_continus(nums, k):
    if not nums:
        return False
    data = [random.choice(nums) for _ in range(k)]
    data.sort()
    print(data)
    zero = data.count(0)
    print("nums of zero is:", zero)
    small, big = zero, zero + 1
    gap_total = 0
    while big < k:
        tmp = data[big] - data[small] - 1
        if tmp < 0:
            return False
        gap_total += tmp
        big += 1
        small += 1
    if gap_total > zero:
        return False
    return True


if __name__ == '__main__':
    test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
            0, 0]
    t = 5
    print(is_continus(test, t))
