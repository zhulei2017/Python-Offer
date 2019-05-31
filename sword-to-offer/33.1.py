from functools import cmp_to_key


def printminnumber(numbers):
    nums = list(map(str, numbers))    # map:将numbers的list的数字转换为字符串，list: 字符串列表['321', '32', '3']
    # cmp_to_key  .sort(key=cmp_to_key(cmp))    cmp_to_key 将python2中的cmp转换为key
    # lambda 匿名函数：x,y为字符串，xy>yx:1, xy=yx:0, xy<yx:-1
    # 在加减运算时，false是0，true是1
    # A comparison function is any callable that accept two arguments, compares them,
    # and returns a negative number for less-than, zero for equality, or a positive number for greater-than.
    nums.sort(key=cmp_to_key(lambda x, y: ((x+y) > (y+x)) - ((y+x) > (x+y))))
    return ''.join(nums)


if __name__ == '__main__':
    test = [31, 232, 113]
    print(printminnumber(test))
