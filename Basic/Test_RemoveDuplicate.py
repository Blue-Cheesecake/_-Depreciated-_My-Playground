# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

# one of Top Interview Questions
# In-place


def Solution(nums=list):
    for i in nums[::-1]:
        if nums.count(i) > 1:
            nums.remove(i)
    return len(nums)


print(Solution([1, 1, 1, 1]))
