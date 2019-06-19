def print_probability(nums):
    if nums < 1:
        return []
    data1 = [0] + [1] * 6 + [0] * 6 * (nums-1)
    data2 = [0] + [0] * 6 * nums
    flag = 0
    for v in range(2, nums+1):
        if flag:
            for k in range(v, 6*v+1):
                data1[k] = sum([data2[k-j] for j in range(1, 7) if k > j])
            flag = 0
        else:
            for k in range(v, 6*v+1):
                data2[k] = sum([data1[k-j] for j in range(1, 7) if k > j])
            flag = 1
    ret = []
    total = 6 ** nums
    data = data2[nums:] if flag else data1[nums:]
    for v in data:
        ret.append(v*1.0/total)
    print(data)
    return ret


if __name__ == "__main__":
    test = 3
    print(print_probability(test))
