class solution(object):
    def first_not_repeating_char(self, s):
        if not s:
            return -1
        count = {}
        loc = {}
        for k, c in enumerate(s):
            count[c] = count[c] + 1 if count.get(c) else 1    # dict.get('a') 获取字典值
            loc[c] = loc[c] if loc.get(c) else k
            print(loc)
        ret = float('inf')
        for k in loc.keys():
            if count.get(k) == 1 and loc[k] < ret:
                ret = loc[k]
        return ret


if __name__ == "__main__":
    test = 'aabbccadeff'
    print(test[solution().first_not_repeating_char(test)])
