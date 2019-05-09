def insert_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:   # 寻找去除的 x 在之前的有序序列中的位置
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x


if __name__ == "__main__":
    ret = [2, 4, 5, 7, 2, 6]
    insert_sort(ret)
    print(ret)
