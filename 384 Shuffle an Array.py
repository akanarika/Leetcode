class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.ori_nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.ori_nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = []
        nums[:] = self.ori_nums[:]
        shuffled_nums = []
        while nums:
            rand_idx = random.randint(0, len(nums) - 1)
            shuffled_nums.append(nums.pop(rand_idx))
        return shuffled_nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()