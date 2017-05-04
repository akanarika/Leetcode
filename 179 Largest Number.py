class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        if not nums:
            return 0
            
        nums = sorted(nums, key = lambda x: -int(str(x)[0]))

        max_len = max([len(str(num)) for num in nums])

        nums = sorted(nums, key = lambda x: int(str(x) 
                                                + str(x)[0] 
                                                * (max_len - len(str(x))) 
                                                + str(x) 
                                                + str(x)[-1] 
                                                * (max_len - len(str(x)))))


        nums = reversed(nums)
        s = ''.join([str(num) for num in nums])
        
        s = s.lstrip('0')
        
        if not s:
            s = "0"
        
        return s