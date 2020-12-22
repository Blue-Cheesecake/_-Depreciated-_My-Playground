# https://leetcode.com/problems/two-sum/


# can be optimized with Hash map algo
# this is brute force
#  O(n^2)
def Solution(nums=list, target=int):
    output = []
    for i in range(len(nums) - 1):
        try:
            sol = nums.index(target - nums[i], i + 1)
            output.append(i)
            output.append(sol)
        except ValueError:
            pass

    return output


print(Solution(nums=[2, 7, 11, 15], target=9))
# [0,1]
print(Solution(nums=[3, 2, 4], target=6))
# [1,2]
print(Solution(nums=[3, 3], target=6))
# [0,1]
