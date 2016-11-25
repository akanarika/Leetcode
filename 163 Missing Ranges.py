class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            return [str(lower) + "->" + str(upper)] if lower != upper else [str(lower)]
            
        l = []
        last = lower - 1
        if nums[-1] != upper:
            nums.append(upper+1)
        for item in nums:
            if item > last + 2:
                l.append(str(last+1) + "->" + str(item-1))
            elif item > last + 1:
                l.append(str(last+1))
            last = item
        
        return l
        