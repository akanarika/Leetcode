class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
            
        d = 0
        while n > 9 * (d+1) * 10**d:
            n -= 9 * (d+1) * 10**d
            d += 1
        d += 1
        
        p = (n-1) / d
        q = n % d - 1
        
        num = 10**(d-1) + p
        
        return int(str(num)[q])