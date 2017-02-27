# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import numpy


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)

        line_to_count = collections.defaultdict(int)
        line_to_points = collections.defaultdict(set)
        point_count = collections.defaultdict(int)

        for point in points:
            point_count[(point.x, point.y)] += 1

        res = 0
        for i in range(len(point_count.keys())):
            pa = point_count.keys()[i]
            kb = []
            for j in range(i):
                pb = point_count.keys()[j]
                if (pa[0], pa[1]) == (pb[0], pb[1]):
                    k = "self"
                    b = (pa[0], pa[1])
                elif pa[0] == pb[0]:
                    k = "ver"
                    b = pa[0]
                else:
                    k = numpy.longdouble(pb[1] - pa[1])
                        / numpy.longdouble(pb[0] - pa[0])
                    b = - k * pa[0] + pa[1]
                if pa not in line_to_points[(k, b)]:
                    line_to_count[(k, b)] += point_count[pa]
                if pb not in line_to_points[(k, b)]:
                    line_to_count[(k, b)] += point_count[pb]
                res = max(res, line_to_count[(k, b)])
                line_to_points[(k, b)].add(pa)
                line_to_points[(k, b)].add(pb)

        return max(res, max(point_count.values()) if point_count else 0)
