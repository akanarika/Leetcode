class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = []
        for i in range(len(nums)):
            try:
                self.accu.append(self.accu[i-1] + nums[i])
            except:
                self.accu.append(nums[i])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.accu[j] - self.accu[i-1] if i != 0 else self.accu[j]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)