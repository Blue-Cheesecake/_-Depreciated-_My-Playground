# https://leetcode.com/problems/max-consecutive-ones/


def Solution(nums=list):
    Maximum = 0
    i = 0
    while i < len(nums):
        plus = 0
        count = 0
        if nums[i] == 1:
            count += 1
            for j in range(i + 1, len(nums)):
                if nums[j] == 1:
                    plus += 1
                    count += 1
                else:
                    break
        Maximum = max(Maximum, count)
        if plus > 0:
            i += plus
        else:
            i += 1
    return Maximum


print(Solution(nums=[1, 1, 0, 1, 1, 1]))
print(Solution(nums=[1] * 10000))
