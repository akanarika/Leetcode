class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if not words:
            return []
        if len(words) == 1:
            return words[0]
            
        letters = set(''.join(words))
        seen = set()
            
        d = collections.defaultdict(list)
        parent = collections.defaultdict(int)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    seen.add(a)
                    seen.add(b)
                    d[a].append(b)
                    parent[b] += 1
                    break
        res = ''        
        for w in letters - seen:
            res += w
            
        while len(res) != len(letters):
            exist = 0
            for u in letters:
                if not parent[u] and u not in res:
                    res += u
                    exist = 1
                    for ne in d[u]:
                        parent[ne] -= 1
            if not exist:
                return ''
                
        return res
                