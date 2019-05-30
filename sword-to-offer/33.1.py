from functools import cmp_to_key


def printminnumber(numbers):
    nums = list(map(str, numbers))    # map:将numbers的list的数字转换为字符串，list: 字符串列表['321', '32', '3']
    # cmp_to_key  .sort(key=cmp_to_key(cmp)
    # lambda 匿名函数：x,y为字符串，x>y:1, x=y:0, x<y:-1
    nums.sort(key=cmp_to_key(lambda x, y: ((x+y) > (y+x)) - ((y+x) > (x+y))))
    return ''.join(nums)


if __name__ == '__main__':
    test = [321, 232, 113]
    print(printminnumber(test))
