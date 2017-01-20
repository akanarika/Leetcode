class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = ""
        curr_len = 0
        res = 0
        
        for i,x in enumerate(s):
            if x not in curr:
                curr += x
                curr_len += 1
            else:
                idx = curr.find(x)
                curr = curr[idx+1:] + x
                curr_len -= idx
            res = max(res, curr_len)
                
        return res
        