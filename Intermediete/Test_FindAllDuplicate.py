# https://leetcode.com/problems/find-all-duplicates-in-an-array/

from collections import Counter

# TLE


def BadSolution(nums=list):
    result = []
    for i in range(len(nums)):
        if nums.count(nums[i]) > 1 and nums[i] not in result:
            result.extend([nums[i]])
    return result

# TLE


def another(nums=list):
    result = []
    for i in set(nums):
        if nums.count(i) > 1:
            result.append(i)
    return result

# Counter be like: but is the way more faster
# dict = {}
# for i in list: if i not in list: dict[i] = 1 else: dict[i] += 1


def collections(nums=list):
    hold = Counter(nums)
    result = []
    for i, j in hold.items():
        if j >= 2:
            result.append(i)
    return result


def NaiveApproach(nums=list):
    hold = {}
    for i in nums:
        if i not in hold:
            hold[i] = 1
        else:
            hold[i] += 1
    result = []
    for j, k in hold.items():
        if k >= 2:
            result.append(j)
    return result


print(NaiveApproach([1, 1, 2, 2, 3, 4, 6, 7]))
print(collections(list(range(1, 2000000))))
