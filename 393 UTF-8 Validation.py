class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        n = 0
        flag = False
        e = enumerate(data)
        for i, item in e:
            s = bin(item)[2:].zfill(8)
            if not n and s[0] == "0":
                continue
            elif not n:
                while s[0] != "0":
                    item <<= 1
                    n += 1
                    s = bin(item)[2:].zfill(8)[-8:]
                if n == 1:
                    return False
                n -= 1
            else:
                try:
                    n -= 1
                    if not s[:2] == "10":
                        return False
                except:
                    return False
        return not n
        