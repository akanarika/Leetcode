class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return None
            
        n = len(matrix)
        for i in range((n+1) / 2):
            end = n - i - 1
            width = n - i*2 - 1
            for j in range(width):
                a, b, c, d = matrix[i][i+j], matrix[i+j][end], matrix[end][end-j], matrix[end-j][i]
                matrix[i][i+j], matrix[i+j][end], matrix[end][end-j], matrix[end-j][i] = d, a, b, c
            