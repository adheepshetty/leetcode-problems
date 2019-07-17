import unittest
class MinStack:
    '''
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

        push(x) -- Push element x onto stack.
        pop() -- Removes the element on top of the stack.
        top() -- Get the top element.
        getMin() -- Retrieve the minimum element in the stack.
    '''
    stack = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min or self.min[-1]>=x:
            self.min.append(x)

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min[-1]:
            self.min.pop()
        return top

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

class Test(unittest.TestCase):
    def test_(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        minStack.getMin() 
        print(minStack.pop())
        print(minStack.top())
        print(minStack.getMin())

   

if __name__ == "__main__":
    print(MinStack.__doc__)
    unittest.main()