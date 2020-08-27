# https://leetcode.com/explore/featured/card/fun-with-arrays/511/in-place-operations/3157/

# this Solution is not optimal
# move zeros into the last positions
def Solution(nums=list):
    total = nums.count(0)
    count = 0
    while count != total:
        i = nums.index(0)
        while i != len(nums) - 1:
            nums[i], nums[i + 1] = nums[i+1], nums[i]
            i += 1
        count += 1
    return nums


print(Solution(nums=[0, 1, 0, 3, 12, 6, 5, 4, 0, 8, 6, 0, 3]))
