# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

def Solution(nums=list, n=int, left=int, right=int):
    RangeSub = []
    indx = 0
    while indx <= n:
        add = 0
        # find sum of index to n 0 01 012 0123 01234, 1 12 1234 and so on
        for i in range(indx, n):
            add += sum(nums[indx:i+1])
            RangeSub.append(add)
            add = 0
        indx += 1
    RangeSub.sort()
    return sum(RangeSub[left-1:right]) % (10 ** 9 + 7)


print(Solution(nums=[1, 2, 3, 4], n=4, left=1, right=5))
print(Solution(nums=[1, 2, 3, 4], n=4, left=3, right=4))
print(Solution(nums=[1, 2, 3, 4], n=4, left=1, right=10))
print(Solution(nums=[i for i in range(1, 101)], n=100, left=5, right=10))
