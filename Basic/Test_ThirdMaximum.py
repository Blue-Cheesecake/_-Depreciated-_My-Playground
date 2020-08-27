# https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3231/


def Solution(nums=list):
    # remove duplicate
    nums = set(nums)
    nums = list(nums)
    # sort them
    nums.sort()
    if len(nums) >= 3:
        return nums[len(nums) - 3]
    elif len(nums) == 2:
        return nums[1]
    else:
        return nums[0]


print(Solution(nums=[3, 2, 1]))
# 1
print(Solution(nums=[2, 2, 3, 1]))
# 1
print(Solution(nums=[3, 2, 1, 5435, 6436, 6435, 3, 35, 6, 5, 4, 8, 456, 345, 34656, 445]
               ))
# 6435
