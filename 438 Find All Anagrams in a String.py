from collections import Counter
from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []

        l = []
        d_p = dict(Counter(p))
        d_s = defaultdict(int)
        
        for idx in range(len(p)):
            try:
                d_s[s[idx]] += 1
            except:
                return []
        
        if d_p == d_s:
            l.append(0)
        
        for idx in range(1, len(s)-len(p)+1):
            d_s[s[idx+len(p)-1]] += 1
            if d_s[s[idx-1]] == 1:
                del d_s[s[idx-1]]
            else:
                d_s[s[idx-1]] -= 1
            if d_s == d_p:
                l.append(idx)
        
        return l
        