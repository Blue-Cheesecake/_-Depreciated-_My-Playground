# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# algorithm's runtime complexity must be in the order of O(log n).
def Solution(nums=list, target=int):
    # find from index 0
    try:
        minimum = nums.index(target)
    except ValueError:
        return [-1, -1]
    # find from length - 1
    for i in reversed(range(minimum, len(nums))):
        if nums[i] == target and i != minimum:
            return [minimum, i]
    return [minimum, minimum]


print(Solution(nums=[5, 7, 7, 8, 8, 10], target=8))
# Output: [3,4]
print(Solution(nums=[5, 7, 7, 8, 8, 10], target=6))
# Output: [-1,-1]
print(Solution(nums=[5, 7, 7, 8, 10], target=8))
# Output: [3,3]
