def shell_sort(lst):
    lens = len(lst)
    gap = 1
    while gap < lens // 3:  # 自定义gap值
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, lens):
            curNum, preindex = lst[i], i
            while preindex > 0 and lst[preindex - gap] > curNum:    # 参照插入排序，关键码为curNum
                lst[preindex] = lst[preindex - gap]     # 针对前面有序部分，从右边最大值开始，依次左移，直到能空出关键码的位置；
                preindex -= gap     # 左移gap位
            lst[preindex] = curNum      # 填入关键码
        gap //= 3   # 缩小gap，进入下移循环
    return lst


if __name__ == "__main__":
    ret = [2, 4, 5, 7, 2, 6]
    shell_sort(ret)
    print(ret)
