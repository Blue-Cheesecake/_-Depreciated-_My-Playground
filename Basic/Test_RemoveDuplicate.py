# modfied list itself


def Solution(nums=list):
    for i in nums[::-1]:
        if nums.count(i) > 1:
            nums.remove(i)
    return len(nums)


print(Solution([1, 1, 1, 1]))
    