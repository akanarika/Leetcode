class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0

        for num in nums:
            if num < target:
                count += 1
            else:
                break

        return count
