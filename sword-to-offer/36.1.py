def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    num_of_pair = 0
    while i < mid and j < high:
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
            num_of_pair += (mid - i)
        k += 1
    while i < mid:
        lto[k] = lfrom[i]
        i += 1
        k += 1
        # num_of_pair += 1
    while j < high:
        lto[k] = lfrom[j]
        j += 1
        k += 1
    return num_of_pair


def merge_pass(lfrom, lto, llen, slen):
    i = 0
    num_of_pass = 0
    while i + 2*slen < llen:
        num_of_pass += merge(lfrom, lto, i, i+slen, i+2*slen)
        i += 2*slen
    if i + slen < llen:
        num_of_pass += merge(lfrom, lto, i, i+slen, llen)
    else:
        for j in range(i, llen):
            lto[j] = lfrom[j]
    return num_of_pass


def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None]*llen
    num_of_sort = 0
    while slen < llen:
        num_of_sort += merge_pass(lst, templst, llen, slen)
        slen *= 2
        num_of_sort += merge_pass(templst, lst, llen, slen)
        slen *= 2
    return lst, num_of_sort


if __name__ == "__main__":
    ret = [7, 5, 6, 4, 8]
    ret_sort, num_inverse = merge_sort(ret)
    print(ret_sort)
    print(num_inverse)
