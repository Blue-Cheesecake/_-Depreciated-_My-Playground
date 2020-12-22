# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

# one of Top Interview Questions
# In-place


def Solution(nums=list):
    for i in nums[::-1]:
        if nums.count(i) > 1:
            nums.remove(i)
    return len(nums)

# Solution 2 is not in-place but compute only numbers of uniques


def Solution2(nums=list):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    out = 1
    i = 1
    ini = nums[0]
    while i < len(nums):
        if nums[i] == ini:
            i += 1
        else:
            out += 1
            ini = nums[i]
            i += 1
    return out


print(Solution([1, 1, 1, 1]))
print(Solution2(nums=[1, 1, 2, 2]))
print(Solution2(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
