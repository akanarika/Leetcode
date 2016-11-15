class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        p1 = 0
        num = ""
        for p2 in range(len(abbr)):
            if ord(abbr[p2]) < 97:
                if not num and abbr[p2] == "0":
                    return False
                num += abbr[p2]
                if p2 == len(abbr) - 1:
                    p1 += int(num)
                    return True if p1 == len(word) else False
            else:
                if num != "":
                    p1 += int(num)
                num = ""
                try:
                    if word[p1] == abbr[p2]:
                        p1 += 1
                        p2 += 1
                    else:
                        return False
                except:
                    return False
        return True
        