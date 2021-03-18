# https://leetcode.com/problems/sudoku-solver/
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def empty(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    return i, j
        return None

    def isvalid(self, board, col, row, num):
        assert board[row][col] == '.'
        for i in range(9):
            if board[row][i] == num:
                return False
            if board[i][col] == num:
                return False
        c0, r0 = col // 3 * 3, row // 3 * 3
        for i in range(3):
            for j in range(3):
                if board[r0 + i][c0 + j] == num:
                    return False
        return True

    def solve(self, board):
        empty = self.empty(board)
        if empty == None:
            return True
        row, col = empty
        for k in range(1, 10):
            if self.isvalid(board, col, row, str(k)):
                board[row][col] = str(k)
                if self.solve(board):
                    return True
                board[row][col] = '.'
        return False


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s = Solution()
s.solveSudoku(board)
print(board)
