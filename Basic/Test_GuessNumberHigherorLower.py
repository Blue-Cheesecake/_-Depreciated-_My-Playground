# https://leetcode.com/problems/guess-number-higher-or-lower/

pick = 8

# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

# Use binarySearch only


def guess(num=int):
    if pick == num:
        return 0
    elif num < pick:
        return -1
    else:
        return 1


def Solution(n=int):
    left = 1
    right = n + 0
    while True:
        mid = (left + right) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == -1:
            left = mid + 1
        else:
            right = mid


print(Solution(n=10))
