# https://leetcode.com/problems/rotting-oranges/


# find index of rotten

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
# if there is no index: pass (use try except)
# else: i+1, i-1, j+1, j-1 = 2
def Solution(grid=list):
    minute = 0
    # loop untill all org turn to rotten
    AllRot = None
    while AllRot != len(grid):
        # check if all org turn to rotten
        AllRot = 0
        IndexRotten = []
        for index in range(len(grid)):
            IndexRotten.append(list_duplicates_of(grid[index], 2))
        # i == row of grid
        # IndexRootten = [[],[],[],....] contained list of index of 2
        for i in range(len(IndexRotten)):
            # turn to rotten
            if len(IndexRotten[i]) != 0:
                # index of Rotten(j)
                # j = index of 2 on row i
                for ListJ in range(i+1):
                    for j in IndexRotten[ListJ]:
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
        minute += 1
        # make something to end loop
        # else:
        #     AllRot += 1
    return minute


print(Solution(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
