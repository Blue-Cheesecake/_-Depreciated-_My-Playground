# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: list, index: list) -> list:
        target = []
        # From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


s = Solution()
print(s.createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))
print(s.createTargetArray(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0]))
