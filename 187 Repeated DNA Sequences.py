class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = collections.defaultdict(int)
        for i in range(len(s) - 9):
            d[s[i:i+10]] += 1
        
        res = []
        for key, val in d.iteritems():
            if val > 1:
                res.append(key)
                
        return res