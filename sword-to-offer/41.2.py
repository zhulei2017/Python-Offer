def sum_to_s(s):
    a, b = 1, 2
    ret = []
    while a < s/2 + 1:
        if sum(range(a, b+1)) == s:
            ret.append(list(range(a, b+1)))
            a += 1
        elif sum(range(a, b+1)) < s:
            b += 1
        else:
            a += 1
    return ret


if __name__ == "__main__":
    test = 6
    print(sum_to_s(test))
