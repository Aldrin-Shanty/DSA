'''
Stack operations : push,pop,is_empty,size,display
'''


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if (self.is_empty(self.stack)):
            return "Stack is empty"
        return self.stack.pop()

    def display(self):
        print(self.stack)

    def size(self):
        return len(self.stack)
