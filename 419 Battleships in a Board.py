class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
            
        count = 0
        for i, row in enumerate(board):
            for j, block in enumerate(row):
                if block == 'X':
                    for (i_offset, j_offset) in ((-1, 0),(1, 0),(0, -1),(0, 1)):
                        _i = i + i_offset
                        _j = j + j_offset
                        if 0 <= _i < len(board) and 0 <= _j < len(board[0]):
                            if board[_i][_j] != '.' and board[_i][_j] != 'X':
                                board[i][j] = board[_i][_j]
                    if board[i][j] == 'X':
                        board[i][j] = count
                        count += 1
        
        return count