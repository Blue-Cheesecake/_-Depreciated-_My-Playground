# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: list) -> int:
        element = 0
        oneTime = False
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if not oneTime:
                    if i == 0:
                        element = (nums[i] - 1) * (nums[j] - 1)
                        oneTime = True
                element = max(element, (nums[i] - 1) * (nums[j] - 1))
        return element


s = Solution()
print(s.maxProduct(nums=[3, 4, 5, 2]))
# 12
print(s.maxProduct(nums=[1, 5, 4, 5]))
# 16
print(s.maxProduct(nums=[1, 1, 1, 1]))
# 0
print(s.maxProduct(nums=[10, 2, 5, 2]))
# 36
