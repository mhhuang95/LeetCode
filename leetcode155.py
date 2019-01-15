class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minidx = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x < self.stack[self.minidx]:
            self.minidx = len(self.stack) - 1

    def pop(self):
        """
        :rtype: void
        """
        if self.minidx == len(self.stack) - 1:
            self.stack.pop()
            if len(self.stack) == 0:
                self.minidx = 0
            else:
                self.minidx = self.stack.index(min(self.stack))
        else:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.minidx]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()