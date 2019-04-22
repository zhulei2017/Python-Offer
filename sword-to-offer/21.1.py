class MyStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val):
        self.stack.append(val)
        if self.min and self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)

    def pop(self):
        if self.stack:
            self.min.pop()
            return self.stack.pop()
        return None

    def min(self):
        return self.min[-1] if self.min else None


if __name__ == '__main__':
    s = MyStack()
    s.push(2)
    s.push(1)
    s.push(3)
    s.pop()
    s.push(2)
    print(s.stack)
    print(s.min)
