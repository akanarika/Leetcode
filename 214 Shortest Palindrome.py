class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1:
            return s
            
        r = s[::-1]
        for i in xrange(len(r)):
            if s.startswith(r[i:]):
                return r[:i] + s