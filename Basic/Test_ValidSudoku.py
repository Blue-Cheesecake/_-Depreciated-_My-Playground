# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/769/

# This code is not optimal

def helper(board: list, row: int, col: int) -> bool:
    check = {}
    check = set(check)
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] not in check and board[i][j] != '.':
                check.add(board[i][j])
            else:
                if board[i][j] != '.':
                    return False
    # if len(check) == 0:
    #     return False
    return True


class Solution:
    def isValidSudoku(self, board: list) -> bool:
        # check row
        for i in range(9):
            col = {}
            col = set(col)
            for j in range(9):
                if board[i][j] not in col and board[i][j] != '.':
                    col.add(board[i][j])
                else:
                    if board[i][j] != '.':
                        return False

        # check col
        for j in range(9):
            row = {}
            row = set(row)
            for i in range(9):
                if board[i][j] not in row and board[i][j] != '.':
                    row.add(board[i][j])
                else:
                    if board[i][j] != '.':
                        return False

        # check
        indexRow = 0
        while indexRow < 9:
            indexCol = 0
            while indexCol < 9:
                if not helper(board, indexRow, indexCol):
                    return False
                indexCol += 3
            indexRow += 3

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
        "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    # True
    print(s.isValidSudoku(board=[["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
        "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    # False
    print(s.isValidSudoku(board=[[".", ".", ".", ".", ".", ".", "5", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["9", "3", ".", ".", "2", ".", "4", ".", "."], [
          ".", ".", "7", ".", ".", ".", "3", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "3", "4", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "."], [".", ".", ".", ".", ".", "5", "2", ".", "."]]))
    # False
    print(s.isValidSudoku(board=[[".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [
          ".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
    # True
