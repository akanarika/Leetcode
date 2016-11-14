class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mins = []
        self.min_data = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min_data is None or x < self.min_data:
            self.min_data = x
        self.data.append(x)
        self.mins.append(self.min_data)

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()
        self.mins.pop()
        try:
            self.min_data = self.mins[-1]
        except:
            self.min_data = None

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()