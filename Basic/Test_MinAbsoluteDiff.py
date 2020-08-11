# https://leetcode.com/problems/minimum-absolute-difference/

import sys

INI_MAX = sys.maxsize


def Solution(arr=list):
    arr.sort()
    absolute = INI_MAX
    result = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) < absolute:
                absolute = abs(arr[i] - arr[j])
                result.clear()
                result.append([arr[i], arr[j]])
            elif abs(arr[i] - arr[j]) == absolute:
                result.append([arr[i], arr[j]])
            elif abs(arr[i] - arr[j]) > absolute:
                break
    return result


print(Solution(arr=[4, 2, 1, 3]))
print(Solution(arr=[1, 3, 6, 10, 15]))
print(Solution(arr=[3, 8, -10, 23, 19, -4, -14, 27]))
print(len(Solution(list(range(2, 100000)))))
