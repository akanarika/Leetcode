class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        
        for i in range(2, len(nums)):
            j,k = 0,i-1
            while j<k:
                if nums[i] + nums[j] + nums[k] < target:
                    count += k - j
                    j += 1
                else:
                    k -= 1
                    
        return count
        