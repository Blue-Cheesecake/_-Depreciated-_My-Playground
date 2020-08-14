# https://leetcode.com/problems/rotting-oranges/
# The process finding is Done
# function to find repeated element


def list_duplicates_of(seq, item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


# row index = i
# column index = j
# count how many time to turn all oranges to rotten
# rotten i+1, i-1, j+1, j-1


def Solution(grid=list):
    # return trsult
    minute = 0
    # loop untill all org turn to rotten
    # Condition check if oranges are all rotten
    Condition = []
    for con in range(len(grid)):
        Condition.append(len(grid[con]) - grid[con].count(0))
    Calculate = False
    for row in grid:
        if (2 not in row) and (1 not in row):
            pass
        else:
            Calculate = True
            break
    if not Calculate:
        return 0
    Compare = None
    while True:
        # how to hold previous variable
        PreviousGrid = []
        for gr in grid:
            PreviousGrid.append(gr + [])
        Compare = []
        for com in range(len(grid)):
            Compare.append(grid[com].count(2))
        if Compare == Condition:
            break
        # if not Possibility(grid=grid):
        #     return -1
        # it is possible or not
        # check if all org turn to rotten
        IndexRotten = []
        # IndexRootten contained list of index of 2
        for k in range(len(grid)):
            IndexRotten.append(list_duplicates_of(grid[k], 2))
        # i == row of grid
        for i in range(len(IndexRotten)):
            # turn to rotten
            if len(IndexRotten[i]) != 0:
                # index of Rotten(j)
                # j = index of 2 on row i
                for j in IndexRotten[i]:
                    if i - 1 != -1:
                        if grid[i-1][j] != 0:
                            grid[i-1][j] = 2
                    if i + 1 < len(grid):
                        if grid[i+1][j] != 0:
                            grid[i+1][j] = 2
                    if j - 1 != -1:
                        if grid[i][j-1] != 0:
                            grid[i][j-1] = 2
                    if j + 1 < len(grid[i]):
                        if grid[i][j+1] != 0:
                            grid[i][j+1] = 2
        if grid == PreviousGrid:
            return -1
        else:
            minute += 1
    return minute


print(Solution(grid=[[0, 0, 0, 0]]))  # -1
print(Solution(grid=[[0, 2]]))  # 0
print(Solution(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(Solution(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
# if parameter cause infinite loop
# make it return -1
# by setting previous. If previous == grid: return -1
print(Solution(grid=[[2, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [
      1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
print(Solution(grid=[[0]]))
