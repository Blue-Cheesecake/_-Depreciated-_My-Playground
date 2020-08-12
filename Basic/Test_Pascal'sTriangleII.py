# https://leetcode.com/problems/pascals-triangle-ii/


def Solution(rowIndex=int):
    Previous = [1, 1]
    k = 1
    if rowIndex > 1:
        while k != rowIndex:
            row = [1, 1]
            for i in range(len(Previous)-1):
                row.insert(i+1, Previous[i] + Previous[i+1])
            Previous = row
            k += 1
        return row
    else:
        if rowIndex == 1:
            return Previous
        return [1]


for i in range(10):
    print(Solution(i))
