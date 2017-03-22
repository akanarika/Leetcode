class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return min(nums)
            
        p1 = 0
        p3 = len(nums) - 1
        p2 = p3 / 2
        
        if nums[p1] <= nums[p2] <= nums[p3]:
            return nums[p1]
        elif nums[p1] >= nums[p2] <= nums[p3]:
            return self.findMin(nums[p1:p2+1])
        elif nums[p1] <= nums[p2] >= nums[p3]:
            return self.findMin(nums[p2:p3+1])
            