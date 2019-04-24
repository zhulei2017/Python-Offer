from itertools import permutations


def my_permutation(s):
    str_set = []
    ret = []    # final result

    def permutation(string):
        for i in string:
            str_tem = string.replace(i, '')
            str_set.append(i)
            if len(str_tem) > 0:
                permutation(str_tem)
            else:
                ret.append(''.join(str_set))
            str_set.pop()

    permutation(s)
    return ret


if __name__ == '__main__':
    s = 'abc'
    print(my_permutation(s))
    print([''.join(p) for p in permutations(s)])

