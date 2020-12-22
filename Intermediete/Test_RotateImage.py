# https://leetcode.com/problems/rotate-image/
# DO NOT allocate another 2D matrix and do the rotation.
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
        return matrix


s = Solution()
print(s.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.rotate(matrix=[[6, 4, 3, 2, 1], [4, 5, 3, 5, 6], [
      3, 4, 6, 2, 1], [5, 6, 3, 2, 1], [7, 4, 3, 2, 1]]))
