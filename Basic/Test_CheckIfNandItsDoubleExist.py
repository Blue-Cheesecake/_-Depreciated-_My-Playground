# https://leetcode.com/problems/check-if-n-and-its-double-exist/

def Solution(arr=list):
    for i in range(len(arr)):
        if arr[i] * 2 in arr[i+1:] or arr[i] / 2 in arr[i+1:]:
            return True
    return False


print(Solution(arr=[10, 2, 5, 3]))  # True
print(Solution(arr=[7, 1, 14, 11]))  # True
print(Solution(arr=[3, 1, 7, 11]))  # False
