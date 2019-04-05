class MyQueue:
    def __init__(self):
        self.stack1 = []  # incharge add tail num
        self.stack2 = []  # incharge remove the head num

    def push(self, val):
        self.stack1.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return print("no num")

# todo the pri will change the original stack
    def pri(self):
        myque = []
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        while self.stack2:
            myque.append(self.stack2.pop())
            return myque


queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.pop()
queue.pop()
queue.pop()
queue.pop()
print(queue.pri())
