class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        if len(nums) > 2:
            p2 = len(nums) - 1 if len(nums) % 2 == 1 else len(nums) - 2
            p1 = 1
            while p2 > p1:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 2
                p2 -= 2
        