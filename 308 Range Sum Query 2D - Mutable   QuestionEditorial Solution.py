class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        for row in self.matrix:
            for i in range(1, len(row)):
                row[i] += row[i-1]
        

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        _val = self.matrix[row][col] - self.matrix[row][col-1] if col > 0 else self.matrix[row][col]
        for _col in range(col, len(self.matrix[row])):
            self.matrix[row][_col] += val - _val

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sum = 0
        for row in range(row1, row2+1):
            if col1 > 0:
                sum += self.matrix[row][col2] - self.matrix[row][col1-1]
            else:
                sum += self.matrix[row][col2]
        return sum
        

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)