class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
            
        res = 0
        num = 0
        sign = 1
        ss = []
        
        for d in s:
            if d.isdigit():
                num = num * 10 + int(d)
            elif d == '-' or d == '+':
                res += num * sign
                num = 0
                sign = 1 if d == '+' else -1
            elif d == '(':
                ss.append(res)
                ss.append(sign)
                sign = 1
                res = 0
            elif d == ')':
                res += num * sign
                res *= ss.pop()
                res += ss.pop()
                num = 0
        return res + num * sign