class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
            
        res = []
        m = len(matrix)  # row
        n = len(matrix[0])  # col
        offs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        offi = 0
        seen = set()
        i, j = 0, 0

        for _ in range(m*n - 1):
            res.append(matrix[i][j])
            seen.add((i, j))
            new_i = i + offs[offi][0]
            new_j = j + offs[offi][1]
            while new_i >= m or new_i < 0 or new_j >= n or new_j < 0 or (new_i, new_j) in seen:
                offi = (offi + 1) % 4
                new_i = i + offs[offi][0]
                new_j = j + offs[offi][1]
            i, j = new_i, new_j
        res.append(matrix[i][j])
    
        return res