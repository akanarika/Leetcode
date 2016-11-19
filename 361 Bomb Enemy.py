class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        l = self.hits(grid)
        r = zip(*(self.hits(zip(*grid))))
        max_e = max([0] + [l[i][j]+r[i][j] if grid[i][j]=='0' else 0 for i in range(len(grid)) for j in range(len(grid[0]))])
        return max_e
        
    def hits(self, grid):
        list = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            last = 0
            num_e = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    num_e += 1
                if grid[i][j] == 'W':
                    for k in range(last, j):
                        list[i][k] = num_e
                    last = j
                    num_e = 0
                if j == len(grid[0]) - 1:
                    for k in range(last, j + 1):
                        list[i][k] = num_e
        return list
        