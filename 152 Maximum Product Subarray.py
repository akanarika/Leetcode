class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = []
        for i, num in enumerate(nums):
            if not p:
                p.append((num, num))
            else:
                if num > 0:
                    p.append((min(num, p[i-1][0]*num), max(num, p[i-1][1]*num)))
                else:
                    p.append((min(num, p[i-1][1]*num), max(num, p[i-1][0]*num)))
                    
        return max([_p[1] for _p in p])