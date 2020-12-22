# https://leetcode.com/problems/sqrtx/

# Use binarySearch only
def Solution(x=int):
    if x <= 1:
        return x
    left = 1
    right = x
    while True:
        mid = (left + right) // 2
        if mid ** 2 == x:
            return mid
        elif mid ** 2 > x:
            right = mid
        else:
            if (mid + 1) ** 2 > x:
                return mid
            else:
                left = mid
