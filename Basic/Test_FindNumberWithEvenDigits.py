# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

def Solution(nums=list):
    count = 0
    for i in range(len(nums)):
        if len(str(nums[i])) % 2 == 0:
            count += 1
    return count


print(Solution(nums=[12, 345, 2, 6, 7896]))
# 2
print(Solution(nums=[555, 901, 482, 1771, 1111] * 100))
# 1
