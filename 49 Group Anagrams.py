class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
            
        res = []
        for key, value in d.iteritems():
            res.append(value)
            
        return res