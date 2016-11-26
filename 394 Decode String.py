class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        s_num = []
        s_str = []
        ss = ""
        
        for item in s:
            if item == '[':
                s_str.append("")
            elif item == ']':
                num = s_num.pop()
                c_str = s_str.pop() * int(num) if num else s_str.pop()
                if len(s_str) > 0:
                    s_str[-1] += c_str
                else:
                    ss += c_str
            elif ord('0') <= ord(item) <= ord('9'):
                if len(s_num) == len(s_str):
                    s_num.append("")
                s_num[-1] += item
            else:
                try:
                    s_str[-1] += item
                except:
                    ss += item
                    
        return ss
        