# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: list) -> int:
        # find nums[i][j] == 1
        # find upper lower left right are all 0
        count = 0
        lengthRow = len(mat)
        lengthCol = len(mat[0])
        for i in range(lengthRow):
            for j in range(lengthCol):
                if mat[i][j] == 1:
                    indexUp = i - 1
                    indexDown = i + 1
                    indexLeft = j - 1
                    indexRigth = j + 1
                    foundOne = False
                    cont = True
                    try:
                        if cont:
                            while indexUp >= 0:
                                if mat[indexUp][j] == 1:
                                    foundOne = True
                                    cont = False
                                    break
                                indexUp -= 1
                    except:
                        pass
                    try:
                        if cont:
                            while indexDown < len(mat):
                                if mat[indexDown][j] == 1:
                                    foundOne = True
                                    cont = False
                                    break
                                indexDown += 1
                    except:
                        pass
                    try:
                        if cont:
                            while indexLeft >= 0:
                                if mat[i][indexLeft] == 1:
                                    foundOne = True
                                    cont = False
                                    break
                                indexLeft -= 1
                    except:
                        pass
                    try:
                        if cont:
                            while indexRigth < lengthCol:
                                if mat[i][indexRigth] == 1:
                                    foundOne = True
                                    cont = False
                                    break
                                indexRigth += 1
                    except:
                        pass
                    if not foundOne:
                        count += 1
        return count


s = Solution()
print(s.numSpecial(mat=[[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]]))
# 3
print(s.numSpecial(mat=[[1, 0, 0],
                        [0, 0, 1],
                        [1, 0, 0]]))
# 1
print(s.numSpecial(mat=[[0, 0, 0, 1],
                        [1, 0, 0, 0],
                        [0, 1, 1, 0],
                        [0, 0, 0, 0]]))
# 2
print(s.numSpecial(mat=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [
      0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]))
# 4
