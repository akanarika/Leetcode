class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
            
        l = [""] * numRows
        gap = 1
        row = 0
        for item in s:
            l[row] += item
            row += gap
            if row == numRows-1 or row == 0:
                gap *= -1
        s = ""
        for items in l:
            for item in items:
                s += item
                
        return s
        