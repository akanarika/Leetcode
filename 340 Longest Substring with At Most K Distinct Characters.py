from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or not k:
            return 0
            
        max_len = 1
        opt = []
        lengths = []
        d = defaultdict(int)
        for i in range(len(s)):
            try:
                if opt[i-1] < k:
                    if s[i] in s[i - lengths[i-1]: i]:
                        opt.append(opt[i-1])
                    else:
                        opt.append(opt[i-1] + 1)
                    lengths.append(lengths[i-1] + 1)
                    max_len = max(max_len, lengths[i])
                else:
                    min_pos = len(s)
                    if s[i] in s[i-lengths[i-1]:i]:
                        opt.append(k)
                        lengths.append(lengths[i-1]+1)
                    else:
                        for j in range(i-lengths[i-1], i):
                            if d[s[j]] < min_pos:
                                min_pos = d[s[j]]
                        opt.append(k)
                        lengths.append(i - min_pos)
                    max_len = max(max_len, lengths[i])
            except:
                opt.append(1)
                lengths.append(1)
            d[s[i]] = i
        return max_len
        