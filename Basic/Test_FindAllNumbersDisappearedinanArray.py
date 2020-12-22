# https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3270/


# This solution is the worst. (Can't beat anyone in leetcode) but passed
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return None


def Solution(nums=list):
    # check if i in nums or not by using binary search, if not add in new array
    nums.sort()
    arr = []
    for i in range(1, len(nums) + 1):
        if binary_search(nums, 0, len(nums)-1, i) == None:
            arr.append(i)
    return arr


print(Solution(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
# [5,6]
