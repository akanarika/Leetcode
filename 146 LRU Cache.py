from collections import deque

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.d = {}
        self.q = deque([])
        self.c = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            v = self.d[key]
            self.q.remove(key)
            self.q.append(key)
            return v
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.d:
            self.d[key] = value
            if len(self.q) == self.c:
                k = self.q.popleft()
                del self.d[k]
            self.q.append(key)
        else:
            self.d[key] = value
            self.q.remove(key)
            self.q.append(key)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)