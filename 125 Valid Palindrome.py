class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        s = s.lower()
        
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            while not (97<=ord(s[p1])<=122 or 48<=ord(s[p1])<=57):
                p1 += 1
                if p1 >= len(s):
                    return True
            while not (97<=ord(s[p2])<=122 or 48<=ord(s[p2])<=57):
                p2 -= 1
                if p2 < 0:
                    return True
            if p1 >= p2:
                return True
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
            
        return True
        