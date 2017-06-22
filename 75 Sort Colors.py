class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        one_s = 0
        two_s = 0
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = 2
            if tmp < 2:
                nums[two_s] = 1
                two_s += 1
            if tmp == 0:
                nums[one_s] = 0
                one_s += 1