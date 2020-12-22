# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# this solution is quite long to run
# anyone please try to use other solutions


def Solution(coordinates=list):
    # just check if slope are equal or not
    # check if x, y is equals totally
    YAxis = True
    XAxis = True
    for i in range(len(coordinates) - 1):
        if coordinates[i][0] != coordinates[i+1][0]:
            YAxis = False
        if coordinates[i][1] != coordinates[i+1][1]:
            XAxis = False
    if XAxis:
        return XAxis
    elif YAxis:
        return YAxis
    else:
        try:
            slope = (coordinates[0][1] - coordinates[1][1]) / \
                (coordinates[0][0] - coordinates[1][0])
            for i in range(1, len(coordinates) - 1):
                if (coordinates[i][1] - coordinates[i + 1][1]) / (coordinates[i][0] - coordinates[i + 1][0]) != slope:
                    return False
        except ZeroDivisionError:
            return False
        return True


print(Solution(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
# True
print(Solution(coordinates=[[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
# False
print(Solution(coordinates=[[0, 0], [0, 1], [0, -1]]))
# True
print(Solution(coordinates=[[1, 2], [2, 2], [3, 2]]))
# True
print(Solution(coordinates=[[1, -8], [2, -3], [1, 2]]))
# False
print(Solution(coordinates=[[1, 1], [2, 2], [2, 0]]))
# False
print(Solution(coordinates=[[1, 1], [-1, 6], [1, 8]]))
# False
print(Solution(coordinates=[[1, 1], [1, 3], [8, 0]]))
# False
