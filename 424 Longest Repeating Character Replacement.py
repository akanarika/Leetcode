class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = collections.Counter()
        res = 0
        p1 = 0
        p2 = 0
        while p2 < len(s):
            count[s[p2]] += 1
            if p2 - p1 - count.most_common(1)[0][1] + 1 > k:
                count[s[p1]] -= 1
                p1 += 1
            p2 += 1
                
        return p2 - p1