class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        h = len(grid)
        w = len(grid[0])
        d = collections.defaultdict(bool)
        num = 0
        
        for i, row in enumerate(grid):
            for j, land in enumerate(row):
                if not d[(i, j)] and grid[i][j] == '1':
                    s = [(i, j)]
                    while s:
                        u = s.pop()
                        d[u] = True
                        m, n =u[0], u[1]
                        for (p, q) in [(m-1, n), (m+1, n), (m, n-1), (m, n+1)]:
                            if 0<=p<h and 0<=q<w:
                                if not d[(p, q)] and grid[p][q] == '1':
                                    s.append((p, q))
                    num += 1
        
        return num
        