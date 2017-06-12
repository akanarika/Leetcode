class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
            
        s = ['(']
        res = []
        curr = '('
        while s:
            curr = s.pop()
            if curr.count('(') < n:
                s.append(curr + '(')
            if curr.count('(') > curr.count(')'):
                tmp = curr + ')'
                if len(tmp) == n + n:
                    res.append(tmp)
                else:
                    s.append(tmp)
        return res
