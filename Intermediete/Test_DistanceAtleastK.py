def Solution(nums=list, k=int):
    if 1 in nums:
        indx = nums.index(1)
        count = 0
        result = True
        for i in range(indx+1, (len(nums))):
            if nums[i] == 0:
                count += 1
            elif nums[i] == 1:
                if count < k:
                    result = False
                count = 0
    else:
        return False
    return result


print(Solution(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2))
print(Solution(nums=[1, 0, 0, 1, 0, 1], k=2))
print(Solution(nums=[1, 1, 1, 1, 1], k=0))
print(Solution(nums=[0, 1, 0, 1], k=1))
print(Solution(nums=[1, 0, 0, 1, 0, 1] * 10 ** 5, k=2))
print(Solution(nums=[1, 1, 1, 1, 1] * 10 ** 5, k=1))
