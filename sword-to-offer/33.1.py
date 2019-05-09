def cmp(a, b):
    return int(str(a) + str(b)) - int(str(b) + str(a))


def print_mini(nums):
    if not nums:
        return []
    res = int(''.join([str(num) for num in sorted(nums, cmp=cmp)]))
    print(res)


if __name__ == '__main__':
    test = [321, 32, 3]
    print_mini(test)
