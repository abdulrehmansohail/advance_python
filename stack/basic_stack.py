"""
Basic Operations of Stack
There are some basic operations that allow us to perform different actions on a stack.

Push: Add an element to the top of a stack
Pop: Remove an element from the top of a stack
IsEmpty: Check if the stack is empty
IsFull: Check if the stack is full
Peek: Get the value of the top element without removing it

"""


class MyStack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def check_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def check_size(self):
        print(f"{len(self.stack)}/{self.size}")

    # returns the value of the top element without removing it
    def peek(self):
        if not self.check_empty():
            print(self.stack[-1])

    def is_full(self):
        if len(self.stack) == self.size:
            return True
        return False

    # Adding items into the stack
    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")
        self.stack.append(value)

    # Removing an element from the stack
    def pop(self):
        if self.check_empty():
            raise Exception("Stack is empty")
        self.stack.pop()

    def show_stack(self):
        print(self.stack)

s = MyStack(size=3)
s.push(2)
s.push(4)
s.push(5)
s.push(8)
s.show_stack()
s.pop()
s.show_stack()
s.peek()
