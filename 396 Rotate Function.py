class Solution(object):
    def maxRotateFunction(self, A):
        if not A:
            return 0
            
        m = 0
        last = 0
        s = sum(A)
        n = len(A)
        for i in range(n):
            last +=  s - n * (A[-i-1])
            m = max(m, last)
        
        s = 0   
        for i in range(n):
            s += i * A[i]
        
        return m + s
        