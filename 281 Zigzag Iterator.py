class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.p1 = 0
        self.p2 = 0
        self.v1 = v1
        self.v2 = v2
        self.l1 = len(v1)
        self.l2 = len(v2)
        self.curr = 0

    def next(self):
        """
        :rtype: int
        """
        tmp = None
        if not self.curr:
            if self.p1 < self.l1:
                self.curr = 1
                self.p1 += 1
                return self.v1[self.p1-1]
            else:
                self.p2 += 1
                return self.v2[self.p2-1]
        else:
            if self.p2 < self.l2:
                self.curr = 0
                self.p2 += 1
                return self.v2[self.p2-1]
            else:
                self.p1 += 1
                return self.v1[self.p1-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.p1 + self.p2 < self.l1 + self.l2

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())