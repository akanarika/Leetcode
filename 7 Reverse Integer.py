class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x:
            return 0
            
        x = str(x)
        
        if len(x) == 1:
            return int(x)
        
        if x[0] == '-':
            idx = 1
            s = x[idx:]
        else:
            idx = 0
            s = x
            
        s = s[::-1]
        x = int(s) * (-1)**idx
        
        return 0 if x>2147483646 or x<-2147483647 else x
        