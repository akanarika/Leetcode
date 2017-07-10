class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        m = len(matrix[0])
        for i, row in enumerate(matrix):
            for j, num in enumerate(row[:m]):
                if num > target:
                    m = j
                    break
                if num == target:
                    return True
                
        return False