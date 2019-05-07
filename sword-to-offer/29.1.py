def get_more_half_num(numbers):
    if not numbers:
        return 0
    res = numbers[0]
    times = 1
    length = len(numbers)
    for i in range(1, length):
        if times == 0:
            res = numbers[i]
            times = 1
        elif res == numbers[i]:
            times += 1
        else:
            times -= 1

    import collections
    return res if collections.Counter(numbers)[res] * 2 > length else 0


if __name__ == '__main__':
    test = [1, 2, 1, 2, 3, 1, 2, 2, 2]
    print(get_more_half_num(test))
