class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        left = 1
        for i, num in enumerate(nums):
            res.append(left)
            left *= num
        
        right = 1
        for i, num in enumerate(reversed(nums)):
            j = - 1 - i
            res[j] *= right
            right *= num
            
        return res
            