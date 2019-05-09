def bubble_sort(lst):
    for i in range(0, len(lst)):
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]


if __name__ == "__main__":
    ret = [2, 4, 5, 7, 2, 6]
    bubble_sort(ret)
    print(ret)
