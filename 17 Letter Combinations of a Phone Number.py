class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        d = {}
        d[1] = "*"
        d[2] = "abc"
        d[3] = "def"
        d[4] = "ghi"
        d[5] = "jkl"
        d[6] = "mno"
        d[7] = "pqrs"
        d[8] = "tuv"
        d[9] = "wxyz"
        d[0] = " "
        curr = []
        for letter in d[(int)(digits[0])]:
            curr.append(letter)
        for num in digits[1:]:
            new = []
            while curr:
                pre = curr.pop()
                for letter in d[int(num)]:
                    new.append(pre+letter)
            curr[:] = new[:]
        
        return curr
            