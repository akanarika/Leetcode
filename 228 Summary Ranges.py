class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
            
        nums.append(None)
        s = nums[0]
        e = nums[0]
        res = []
        for num in nums[1:]:
            if num and num == e + 1:
                e = num
            else:
                res.append((str(s) + "->" + str(e)) if s != e else str(s))
                s = num
                e = num
                
        return res
                    