class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
            
        _board = [[0] * len(board[0]) for _ in range(len(board))]
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell:
                    for x, y in [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]:
                        if 0<=x<len(board) and 0<=y<len(row):
                            _board[x][y] += 1
        
        for i, row in enumerate(_board):
            for j, cell in enumerate(row):
                if board[i][j]:
                    if cell == 2 or cell == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
                else:
                    if cell == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0
        