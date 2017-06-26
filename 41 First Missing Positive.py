class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 0 < nums[i] <= n and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]
                nums[i] = nums[tmp-1]
                nums[tmp-1] = tmp
                
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        return n + 1