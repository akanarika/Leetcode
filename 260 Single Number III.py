class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bit = 0
        for num in nums:
            bit ^= num
            
        bit = bit & (~bit + 1)
        
        g_1 = []
        g_2 = []
        for num in nums:
            if bit & num != bit:
                g_1.append(num)
            else:
                g_2.append(num)
                
        res_1, res_2 = 0, 0
        for num in g_1:
            res_1 ^= num
        for num in g_2:
            res_2 ^= num
            
        return [res_1, res_2]
        