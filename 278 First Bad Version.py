# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return None
            
        if isBadVersion(1):
            return 1
            
        bound = [1, n]
        while True:
            if bound[0] - bound[1] == -1:
                if isBadVersion(bound[0]):
                    return bound[0]
                return bound[1]
            x = (bound[0] + bound[1]) / 2
            if isBadVersion(x):
                bound[1] = x
            else:
                bound[0] = x
            