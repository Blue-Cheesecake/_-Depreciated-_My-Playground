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
    # index for

    return output


print(Solution(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution(nums=[[1, 2, 3, 4, 5], [6, 7], [
      8], [9, 10, 11], [12, 13, 14, 15, 16]]))
