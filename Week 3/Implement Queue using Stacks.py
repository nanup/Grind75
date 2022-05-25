class MyQueue(object):

    def __init__(self):
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.inStack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.outStack) and (not self.inStack)
        
    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()