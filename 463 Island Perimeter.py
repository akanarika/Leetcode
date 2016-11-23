class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
            
        d = collections.defaultdict(lambda: [0,0,0,0]) #left, up, right, down
        idx = 0
        l = len(grid)
        w = len(grid[0])
        for i in range(l): #rows
            for j in range(w): #cols
                if grid[i][j]:
                    try:
                        d[(j,i-1)][0] = 1 #left
                    except:
                        pass
                    try:
                        d[(j-1,i)][1] = 1 #up
                    except:
                        pass
                    try:
                        d[(j,i+1)][2] = 1 #right
                    except:
                        pass
                    try:
                        d[(j+1,i)][3] = 1 #down
                    except:
                        pass
                    
        s = 0
        for i in range(l): #rows
            for j in range(w): #cols
                if grid[i][j]:
                    s += 4 - sum(d[(j,i)])
                    
        return s
        