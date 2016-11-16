import re

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        m = re.match(r'(\s)*(\+|\-|)(\d)*', str)
        try:
            s = int(m.group(0))
            return min(max(s, -2147483648), 2147483647)
        except:
            return 0
        