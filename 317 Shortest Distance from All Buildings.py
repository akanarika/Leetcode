from collections import deque

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        
        dists = []
        for i, row in enumerate(grid):
            for j, pt in enumerate(row):
                if pt == 1:
                    d = [[None]*cols for _ in range(rows)]
                    d[i][j] = 0
                    s = deque([(i,j)])
                    while s:
                        u = s.popleft()
                        for x in (-1,1):
                            if 0<=u[0]+x<rows and grid[u[0]+x][u[1]] == 0:
                                if d[u[0]+x][u[1]] is None or d[u[0]][u[1]] + 1 < d[u[0]+x][u[1]]:
                                    if (u[0]+x, u[1]) not in s:
                                        s.append((u[0]+x, u[1]))
                                    d[u[0]+x][u[1]] = d[u[0]][u[1]] + 1
                            if 0<=u[1]+x<cols and grid[u[0]][u[1]+x] == 0:
                                if d[u[0]][u[1]+x] is None or d[u[0]][u[1]] + 1 < d[u[0]][u[1]+x]:
                                    if (u[0], u[1]+x) not in s:
                                        s.append((u[0], u[1]+x))            
                                    d[u[0]][u[1]+x] = d[u[0]][u[1]] + 1
                    d[i][j] = None
                    dists.append(d)
        
        result = None
        for i in range(rows):
            for j in range(cols):
                try:
                    s = sum(l[i][j] for l in dists if l[i][j] != 0)
                    if not result or s < result:
                        result = s
                except:
                    continue
        
        return result if result else -1
        