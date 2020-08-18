def do(nums=list, boolean):
    if boolean:
        n = len(nums)
    else:
        n = len(nums) // 2
    output = []
    # index = index of row
    # i = index of row (for adding)
    # j = index of column (for adding)
    # k = time to do
    # count do untill reach k
    # this process is done only half way
    index = 0
    while index < n:
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
    return output


def Solution(nums=list):
    output = []
    hold = []
    output.extend(do(nums, True))
    nums = nums[::-1]
    hold.extend(do(nums, False))

    return output, hold


print(Solution(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution(nums=[[1, 2, 3, 4, 5], [6, 7], [
      8], [9, 10, 11], [12, 13, 14, 15, 16]]))
