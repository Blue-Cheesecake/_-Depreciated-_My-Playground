# https://leetcode.com/problems/diagonal-traverse-ii/


def Solution(nums=list):
    # index = index of row
    # i = index of row (for adding)
    # j = index of column (for adding)
    # k = time to do
    # count do untill reach k
    # this process is done only half way
    output = []
    index = 0
    while index < len(nums):
        count = 0
        i = index + 0
        j = 0
        k = index + 1
        while count < k:
            try:
                output.append(nums[i][j])
            except IndexError:
                pass
            count += 1
            i -= 1
            j += 1
        index += 1
    # the other half
    # index for static last row (index + 1 if done) (hold j)
    # i index of row (for adding, i -= 1)
    # j index of column (for adding j += 1)
    index = 1
    while index != len(nums[len(nums) - 1]):
        count = 0
        i = len(nums) - 1
        j = index + 0
        # how to define time to add into k
        k = k - 1
        while count < k:
            try:
                output.append(nums[i][j])
            except IndexError:
                pass
            count += 1
            i -= 1
            j += 1
        index += 1

    return output


print(Solution(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [1,4,2,7,5,3,8,6,9]
print(Solution(nums=[[1, 2, 3, 4, 5], [6, 7], [
      8], [9, 10, 11], [12, 13, 14, 15, 16]]))
# [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
print(Solution(nums=[[1, 2, 3], [4], [5, 6, 7], [8], [9, 10, 11]]))
# [1,4,2,5,3,8,6,9,7,10,11]
print(Solution(nums=[[1, 2, 3], [4]]))
# [1,4,2,3]
print(Solution(nums=[[8, 2, 3, 4, 5]]))
# [8]
