"""
使用装饰器实现
"""
from functools import wraps


def single_ton(cls):
    _instance = {}

    @wraps(cls)    # wraps也是一种装饰器，将原信息复制到新的函数
    def single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return single  # 返回函数，非函数运行结果；


@single_ton
class SingleTon(object):
    val = 123

    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    s = SingleTon(1)
    t = SingleTon(2)
    print(id(s))
    print(id(t))
    print(type(s))
    print(type(t))
