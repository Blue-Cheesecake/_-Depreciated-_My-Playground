# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers(self, matrix: list):
        # find minimum of each row
        # check if it minimum in its col or not
        result = []
        element = 0
        for i in range(len(matrix)):
            element = min(matrix[i])
            # check
            static = matrix[i].index(element)
            indexUp = i + 0
            indexDown = i + 0
            add = True
            while indexUp >= 0:
                if matrix[indexUp][static] > element:
                    add = False
                    break
                indexUp -= 1
            while indexDown < len(matrix):
                if matrix[indexDown][static] > element:
                    add = False
                    break
                indexDown += 1
            if add:
                result.append(element)
        return result


s = Solution()
print(s.luckyNumbers(matrix=[[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
# 15
print(s.luckyNumbers(matrix=[[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
# 12
print(s.luckyNumbers(matrix=[[7, 8], [1, 2]]))
# 7
