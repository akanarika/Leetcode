from collections import defaultdict

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        d = defaultdict(list)
        l = len(words[0])
        for word in words:
            for i in range(l):
                d[word[:i]].append(word)
        
        squares = []
        
        def build(square):
            if len(square) == l:
                squares.append(square)
                return
            for line in d[''.join(zip(*square)[len(square)])]:
                build(square + [line])
        
        for word in words:
            build([word])
            
        return squares
                