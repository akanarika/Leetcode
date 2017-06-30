class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i = 0
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        num = self.vec2d[self.i][self.j]
        if self.j == len(self.vec2d[self.i]) - 1:
            self.i += 1
            self.j = 0
        else:
            self.j += 1
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        while not (self.i == len(self.vec2d) and self.j == 0) and self.vec2d[self.i] == []:
            self.i += 1
            self.j = 0
        return not (self.i == len(self.vec2d) and self.j == 0)
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())