# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        l = []
        for item in intervals:
            l.append([item.start, 's'])
            l.append([item.end, 'e'])
            
        l = sorted(l, key = lambda x : (x[0] - 0.5 if x[1] == 'e' else x[0]))
        
        s = []
        m = 0
        print l
        for item in l:
            if item[1] == 's':
                s.append(0)
                m = max(m, len(s))
            else:
                s.pop()
            
        return m
        
        