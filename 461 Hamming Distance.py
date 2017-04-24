class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        mask = 1
        res = 0
        for i in range(32):
            res += (int)(x & mask != y & mask)
            mask <<= 1
            
        return res