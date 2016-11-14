class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ""
        while n:
            s = chr((n-1)%26 + 65) + s
            n = (n-1) / 26
            
        return s
        