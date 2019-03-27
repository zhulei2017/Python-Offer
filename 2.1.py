class Other(object):
    val = 123

    def __init__(self):
        print('other instance')


class NoReturn(object):

    def __new__(cls, *args, **kwargs):
        print 'NoReturn __new__'
        return Other()

    def __init__(self, a):
        print a
        print 'NoReturn __init__'

t = NoReturn(12)
print(type(t))