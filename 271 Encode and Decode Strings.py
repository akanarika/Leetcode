class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join('{}:{}'.format(len(s), s) for s in strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i = 0
        strs = []
        while True:
            try:
                j = s.find(':', i)
                i = j + 1 + int(s[i:j])
                str = s[j+1: i]
                strs.append(str)
            except:
                break
        return strs
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))