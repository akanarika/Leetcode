class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        a = map(int, version1.split('.'))
        b = map(int, version2.split('.'))
        
        i = 0
        while i < min(len(a), len(b)):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
            i += 1
            
        if len(a) == len(b):
            return 0
            
        c = a if len(a) > len(b) else b
        if sum(c[i:]) == 0:
            return 0
        else:
            return 1 if len(a) > len(b) else -1
        