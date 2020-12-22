# https://leetcode.com/problems/diagonal-traverse-ii/

# Time Limit Exceed
# This code must be able to support a lot of input (10 ^ 6)
def Solution(nums=list):
    if len(nums) == 1:
        return nums[0]
    output = []
    MaxColumn = 0
    for i in nums:
        MaxColumn = max(len(i), MaxColumn)
    # Time to do is from len(nums) + MaxColumn - 1
    TimeTodo = len(nums) + MaxColumn - 1
    count = 0
    # do untill holdI == len(nums)
    # if holdI == len(nums): holdJ += 1
    holdI = 0
    holdJ = 0
    while count < TimeTodo:
        i = holdI + 0
        j = holdJ + 0
        # condition to make i and j not exceed the frame
        while j != MaxColumn and i >= 0:
            try:
                output.append(nums[i][j])
            except IndexError:
                pass
            i -= 1
            j += 1
        count += 1
        if holdI < len(nums) - 1:
            holdI += 1
        else:
            holdJ += 1

    return output


print(Solution(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [1,4,2,7,5,3,8,6,9]
print(Solution(nums=[[1, 2, 3, 4, 5], [6, 7], [
      8], [9, 10, 11], [12, 13, 14, 15, 16]]))
# [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
print(Solution(nums=[[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]]))
#  [1,4,2,5,3,8,6,9,7,10,11]
print(Solution(nums=[[1, 2, 3], [4]]))
# # [1,4,2,3]
print(Solution(nums=[[8, 2, 3, 4, 5]]))
# [8,2,3,4,5]
print(Solution(nums=[[1, 2], [3, 4, 5, 6]]))
# [1,3,2,4,5,6]
print(Solution(nums=[[3, 4, 5, 6], [1, 2]]))
# [3,1,4,2,5,6]
print(Solution(nums=[[1, 2, 3, 4, 5, 6, 8] * 100000]))
