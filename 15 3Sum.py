class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            a = nums[i]
            while j < k:
                b = nums[j]
                c = nums[k]
                if a + b + c < 0:
                    j += 1
                elif a + b + c > 0:
                    k -= 1
                else:
                    s.append([a, b, c])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                        
        return s