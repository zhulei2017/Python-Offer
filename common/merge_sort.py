# 最下层：一对有序序列的归并操作；
def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:     # 反复复制两分段首记录中较小的
        if lfrom[i] <= lfrom[j]:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:      # 复制第一段剩余记录，序列本身是有序的，因为上一个循环的终止条件，下面这两个循环只有一个会执行，且序列中剩下的数一定大于已归并序列中的数；
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:     # 复制第二段剩余记录
        lto[k] = lfrom[j]
        j += 1
        k += 1


def merge_pass(lfrom, lto, llen, slen):     # slen 表示分段长度，llen 表示表长度
    i = 0
    while i + 2*slen < llen:
        merge(lfrom, lto, i, i+slen, i + 2*slen)
        i += 2*slen
    if i + slen < llen:     # 剩下两段，后段长度小于 slen
        merge(lfrom, lto, i, i+slen, llen)
    else:   # 只剩下一段，复制到表lto
        for j in range(i, llen):
            lto[j] = lfrom[j]


def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None]*llen
    while slen < llen:
        merge_pass(lst, templst, llen, slen)
        slen *= 2
        merge_pass(templst, lst, llen, slen)
        slen *= 2
    return lst


if __name__ == "__main__":
    ret = [2, 4, 5, 7, 2, 6]
    merge_sort(ret)
    print(ret)
