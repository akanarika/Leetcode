from collections import deque

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(people)
        idx = range(n)
        q = deque(sorted(people, key=(lambda x:x[0])))
        l = [None] * n
        last = []
        curr = None
        while q:
            u = q.popleft()
            if curr is None or curr != u[0]:
                curr = u[0]
                if last:
                    last = sorted(last)
                while last:
                    idx.pop(last.pop())
            l[idx[u[1]]] = u
            last.append(u[1])
                
        return l
        