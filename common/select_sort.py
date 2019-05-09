def select_sort(lst):
    for i in range(0, len(lst)-1):
        k = i
        for j in range(i, len(lst)):    # k 是已知最小元素的位置
            if lst[j] < lst[k]:
                k = j
        if i != k:
            lst[i], lst[k] = lst[k], lst[i]


if __name__ == "__main__":
    ret = [2, 4, 5, 7, 2, 6]
    select_sort(ret)
    print(ret)