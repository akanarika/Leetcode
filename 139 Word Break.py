class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
            
        opt = set([])
        for i in range(len(s)+1):
            for j in range(i):
                if (s[j:i] in wordDict) and (j-1 in opt or not j):
                    opt.add(i-1)
                    
        return len(s)-1 in opt