class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        res = []
        while i < n:
            if 1 <= nums[i] <= n:
                if nums[nums[i]-1] > n:
                    nums[nums[i]-1] += 1
                    nums[i] = 0
                    i += 1
                    continue
                else:
                    if nums[i] == i + 1:
                        nums[i] = n + 1
                    else:
                        tmp = nums[nums[i]-1]
                        nums[nums[i]-1] = n + 1
                        nums[i] = tmp
            else:
                i += 1
        
        for idx, num in enumerate(nums):
            if num > n + 1:
                res.append(idx+1)
                
        return res