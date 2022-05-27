class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append([val, min(self.getMin(), val)])
        

    def pop(self):
        """
        :rtype: None
        """
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        return sys.maxint


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()