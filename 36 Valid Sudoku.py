class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            row = [i for i in row if i != '.']
            if len(set(row)) != len(list(row)):
                return False
        
        for row in zip(*board):
            row = [i for i in row if i != '.']
            if len(set(row)) != len(list(row)):
                return False
                
        for i in xrange(3):
            for j in xrange(3):
                block = [board[x + i * 3][y + j * 3] for x in xrange(3) for y in xrange(3)]
                block = [a for a in block if a != '.']
                if len(set(block)) != len(list(block)):
                    return False
                    
        return True