class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        t = [(1, 'I'), (5, 'V'),
             (10, 'X'), (50, 'L'),
             (100, 'C'), (500, 'D'),
             (1000, 'M')]
        m = 1
        s = ""
        for i in reversed(str(num)):
            n = int(i)
            
            if not n:
                m += 1
                continue
            
            if n == 4:
                c = t[m * 2 - 2][1] + t[m * 2 - 1][1]
            elif n == 9:
                c = t[m * 2 - 2][1] + t[m * 2][1]
            elif n == 5:
                c = t[m * 2 - 1][1]
            elif n < 5:
                c = n * t[m * 2 - 2][1]
            else:
                c = t[m * 2 - 1][1] + (n - 5) * t[m * 2 - 2][1]
            s = c + s
            m += 1
        
        return s
        