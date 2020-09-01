# https://leetcode.com/problems/merge-intervals/

# check if element intervals[i][ele] in range in[i+1][ele] or not
# if True --> merge from in[i][f] to in[i+1][l]
# else pass
# sort them by intervals[i][0] increasing order
# intervals = sorted(intervals, key=lambda kv: kv[0])
# this algotithm's complexity == O(n^2)
def Solution(intervals=list):
    intervals = sorted(intervals, key=lambda kv: kv[0])
    sIndx = 0
    n = len(intervals)
    if n == 1:
        return intervals
    while sIndx < n - 1:
        # if i not in range suspect index move (+1)
        iInOrNot = False
        Clowest = min(intervals[sIndx][0], intervals[sIndx+1][0])
        Chighest = max(intervals[sIndx][1], intervals[sIndx+1][1])
        for i in range(Clowest, intervals[sIndx][1] + 1):
            if i in range(intervals[sIndx+1][0], intervals[sIndx+1][1] + 1):
                merge = [Clowest, Chighest]
                intervals.pop(sIndx)
                intervals.pop(sIndx)
                intervals.insert(sIndx, merge)
                iInOrNot = True
                # length of intervals is decreased
                n -= 1
                # no need to find the others anymore
                break
        if not iInOrNot:
            sIndx += 1
    return intervals


print(Solution(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1,6],[8,10],[15,18]]
print(Solution(intervals=[[1, 4], [4, 5]]))
# [[1,5]]
print(Solution(intervals=[[1, 4], [0, 4]]))
# [[0,4]]
print(Solution(intervals=[[1, 4], [0, 0]]))
# [[0,0],[1,4]]
