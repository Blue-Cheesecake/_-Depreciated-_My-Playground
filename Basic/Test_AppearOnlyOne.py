def Solution(nums=list):
    result = []
    for i in set(nums):
        if nums.count(i) == 1:
            result.append(i)
    return result


print(Solution([1] * (10 ** 7)))
