class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        tbl = self.buildTbl(needle)
        i = 0
        j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == len(needle):
                return i - j
            elif i < len(haystack) and haystack[i] != needle[j]:
                if j > 0:
                    j = tbl[j-1]
                else:
                    i += 1
        return -1
        
    def buildTbl(self, needle):
        tbl = [0]
        length = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[length]:
                i += 1
                length += 1
                tbl.append(length)
            else:
                if length > 0:
                    length = tbl[length-1]
                else:
                    tbl.append(length)
                    i += 1
        return tbl