class SingleTon(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # 如果__instance为空证明是第一次创建实例
            # 通过父类的__new__(cls)创建实例
            cls._instance = super().__new__(cls)
        #print cls._instance
        return cls._instance


class MyClass(SingleTon):
    class_val = 22

    def __init__(self, val):
        self.val = val


if __name__ == '__main__':
    a = MyClass(1)
    b = MyClass(2)
    print(id(a))
    print(id(b))
