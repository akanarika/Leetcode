class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        last = collections.deque([]) # last 5 coords
        curr = (0, 0)
        for index, _x in enumerate(x):
            north = (int)(index % 4 == 0)
            west = (int)(index % 4 == 1)
            south = (int)(index % 4 == 2)
            east = (int)(index % 4 == 3)
            tmp = (curr[0] - west * _x + east * _x, curr[1] - south * _x + north * _x)
            if index == 3:
                #compare 3 with 0
                if self.isCrossing(curr, tmp, last[0]):
                    return True
            elif index == 4:
                if self.isCrossing(curr, tmp, last[1]):
                    return True
            elif index > 4:
                if self.isCrossing(curr, tmp, last[0])\
                    or self.isCrossing(curr, tmp, last[2]):
                   return True
            for item in last:
                if tmp == item[0] or tmp == item[1]:
                    return True
            if len(last) == 5:
                last.popleft()
            last.append((curr, tmp))
            curr = tmp
        return False
        
    def isCrossing(self, curr, tmp, line):
        if line[0][0] == line[1][0]:
            return (line[0][1] - curr[1]) * (line[1][1] - curr[1]) <= 0\
                   and (line[0][0] - curr[0]) * (line[0][0] - tmp[0]) <= 0
        else:
            return (line[0][0] - curr[0]) * (line[1][0] - curr[0]) <= 0\
                   and (line[0][1] - curr[1]) * (line[0][1] - tmp[1]) <= 0