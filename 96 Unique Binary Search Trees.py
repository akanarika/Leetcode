class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = [1, 1, 2]
        for i in range(3, n+1):
            k, curr = 1, 0
            while k <= i / 2:
                curr += 2 * c[k-1] * c[i-k]
                k += 1
            c.append(curr + c[i/2] ** 2 if i % 2 else curr)
        
        return c[n]