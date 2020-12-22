# https://leetcode.com/problems/contains-duplicate-iii/

# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

# Time limit exceed

def Solution(nums=list, k=int, t=int):
    output = False
    for i in range(len(nums) - 1):
        limitJ = len(nums)
        if i + k + 1 <= len(nums):
            limitJ = i + k + 1
        for j in range(i + 1, limitJ):
            if abs(i - j) <= k and abs(nums[i] - nums[j]) <= t:
                output = True
                break
        if output == True:
            break
    return output


print(Solution(nums=[1, 2, 3, 1], k=3, t=0))
# True
print(Solution(nums=[1, 0, 1, 1], k=1, t=2))
# True
print(Solution(nums=[1, 5, 9, 1, 5, 9], k=2, t=3))
# False
print(Solution(nums=[1, 2, 1, 1], k=1, t=0))
# True
