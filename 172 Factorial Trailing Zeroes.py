class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        
        while n:
            s += n/5
            n /= 5

        return s
