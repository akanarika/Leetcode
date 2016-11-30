from collections import defaultdict

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        d1 = defaultdict(lambda: -1) # island name for every position
        d2 = defaultdict(list) # point list for every island
        l = []
        print positions
        for pos in positions:
            neighbor_points = filter(lambda (x,y): 0<=x<m and 0<=y<n,[(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), 
                               (pos[0], pos[1]-1), (pos[0], pos[1]+1)])
            neighbor_islands = [d1[x[0]*n+x[1]] for x in neighbor_points]
            island_name = max(neighbor_islands + [-1])
            if island_name == -1:
                d1[pos[0]*n+pos[1]] = pos[0]*n + pos[1]
                d2[pos[0]*n+pos[1]] = [pos[0]*n+pos[1]]
            else:
                for island in neighbor_islands:
                    if island != island_name:
                        d2[island_name].extend(d2[island] +[pos[0]*n + pos[1]])
                        for point in d2[island]:
                            d1[point] = island_name
                        d1[pos[0]*n + pos[1]] = island_name
                        del d2[island]
            l.append(len(d2))
        return l
        