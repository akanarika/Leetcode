class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        res = 0
        for i, tok in enumerate(tokens):
            if tok == "+" or tok == "-" or tok == "*" or tok == "/":
                a = nums.pop()
                b = nums.pop()
                if tok == "+":
                    res = b + a
                elif tok == "-":
                    res = b - a
                elif tok == "*":
                    res = b * a
                else:
                    res = int(float(b) / float(a))
            else:
                res = int(tok)
            nums.append(res)
                
        return res