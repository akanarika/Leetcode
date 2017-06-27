class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        zero = [1]
        one = [1]
        s = (bin(num))[2:][::-1]
        n = len(s)
        
        for i in range(1, n):
            zero.append(zero[i-1] + one[i-1])
            one.append(zero[i-1])
        
        res = zero[n-1] + one[n-1]
        for i in range(n-2, -1, -1):
            if s[i] == '1' and s[i+1] == '1':
                break
            if s[i] == '0' and s[i+1] == '0':
                res -= one[i]
            
        return res