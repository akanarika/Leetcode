# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        while True:
            buf4 = [""]*4
            x = read4(buf4)
            t = min(x, n-i)
            for j in range(t):
                buf[i] = buf4[j]
                i += 1
            if x < 4 or i==n:
                return i
            