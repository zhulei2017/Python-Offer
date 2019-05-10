def bubble_sort(lst):
    for i in range(0, len(lst)):
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]


def bubble_sort_flag(lst):
    for i in range(0, len(lst)):
        found = False
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                found = True
        if not found:
            break


if __name__ == "__main__":
    ret = [2, 4, 5, 7, 2, 6]
    # bubble_sort(ret)
    bubble_sort_flag(ret)
    print(ret)
