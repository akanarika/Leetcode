class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or matrix == [[]]:
            return 0
        max_area = 0
        for i, row in enumerate(matrix):
            for j, block in enumerate(row):
                ii = i
                min_width = len(matrix[0])
                while ii < len(matrix) and matrix[ii][j] == '1':
                    jj = j
                    while jj < len(matrix[ii]) and matrix[ii][jj] == '1':
                        jj += 1
                    min_width = min(min_width, jj - j)
                    ii += 1
                    max_area = max(max_area, min_width * (ii - i))
                    
        return max_area
                
                        
                    