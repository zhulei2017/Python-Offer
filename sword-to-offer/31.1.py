def sum_array_max(lst):
    ret = float("-inf")
    if not lst:
        return ret
    sum_cur = 0
    sum_all = 0
    for i in lst:
        if sum_cur >= 0:
            sum_cur += i
            sum_all = max(sum_cur, sum_all)
        else:
            sum_cur = 0
            sum_cur += i
            sum_all = max(sum_cur, sum_all)
    return sum_all


if __name__ == "__main__":
    ret = [1, -2, 3, 10, -4, 7, 2, -5]
    result = sum_array_max(ret)
    print(result)
    test = []
    print(sum_array_max(test))
