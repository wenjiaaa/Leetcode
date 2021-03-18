# https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if not self.isvalid(i, j, board[i][j], board):
                        return False
        return True

    def isvalid(self, row, col, num, board):
        for i in range(9):
            if board[i][col] == num and i != row:
                return False
        for j in range(9):
            if board[row][j] == num and j != col:

                return False
        r0, c0 = row // 3 * 3, col // 3 * 3
        for i in range(3):
            for j in range(3):
                if board[r0 + i][c0 + j] == num and r0 + i != row and c0 + j != col:
                    return False
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
S = Solution()
print(S.isValidSudoku(board))
