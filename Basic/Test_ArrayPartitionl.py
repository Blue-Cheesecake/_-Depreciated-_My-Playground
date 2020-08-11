# https://leetcode.com/problems/array-partition-i/


def Solution(nums=list):
    nums.sort()
    n = len(nums) // 2
    indx = 0
    result = 0
    count = 0
    while count != n:
        result += nums[indx]
        count += 1
        indx += 2
    return result


print(Solution([1, 4, 3, 2]))
print(Solution(list(range(-10000, 10000))))
