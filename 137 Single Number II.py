class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
            
        for key, value in d.iteritems():
            if value != 3:
                return key
                