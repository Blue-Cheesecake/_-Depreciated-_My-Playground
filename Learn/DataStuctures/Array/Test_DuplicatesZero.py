# https://leetcode.com/problems/duplicate-zeros/


def Solution(arr=list):
    skip = 0
    while skip < len(arr):
        if arr[skip] == 0:
            arr.insert(skip+1, 0)
            arr.pop()
            skip += 2
        else:
            skip += 1


print(Solution([1, 0, 2, 3, 0, 4, 5, 0]))
print(Solution([1, 2, 3]))
print(Solution([1, 0]))
print(Solution([0]*10000))
