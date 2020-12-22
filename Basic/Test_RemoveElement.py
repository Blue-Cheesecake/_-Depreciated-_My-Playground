# https://leetcode.com/problems/remove-element/
# in-place concept

def Solution(nums=list, val=int):
    i = 0
    length = len(nums)
    while i < length:
        if nums[i] == val:
            nums.pop(i)
            length -= 1
        else:
            i += 1


def Solution2(nums=list, val=list):
    for i in range(nums.count(val)):
        nums.remove(val)


print(Solution(nums=[3, 2, 2, 3], val=3))
# Your function should return length = 2, with the first two elements of nums being 2.


print(Solution(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))
# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
