# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Use binarySearch only
def binarySearchI(arr, x, left, right):
    if len(arr) == 0:
        return -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def Solution(nums=list, target=int):
    # find index of Zero
    # binary 2 time
    start = 0
    while True:
        try:
            indexOfZero = nums.index(start)
            break
        except ValueError:
            start += 1
    found = binarySearchI(nums, target, 0, indexOfZero - 1)
    if found == -1:
        return binarySearchI(nums, target, indexOfZero, len(nums) - 1)
    else:
        return found


print(Solution(nums=[4, 5, 6, 7, 8, 9, 3], target=6))
