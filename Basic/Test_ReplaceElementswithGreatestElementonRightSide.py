# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

def Solution(arr=list):
    maxSoFar = arr[len(arr) - 1]
    arr[len(arr) - 1] = -1
    # for backward
    for i in range(len(arr) - 2, -1, -1):
        temp = arr[i]
        arr[i] = maxSoFar
        maxSoFar = max(maxSoFar, temp)
    return arr


print(Solution(arr=[17, 18, 5, 4, 6, 1]))
