# https://leetcode.com/problems/rotate-array/


# brute force --> Time limit exceed
# class Solution:
#     def oneRotate(self, nums=list):
#         temp = nums[len(nums) - 1]
#         for i in reversed(range(len(nums))):
#             nums[i] = nums[i-1]
#             if i == 0:
#                 nums[i] = temp

#     def rotate(self, nums=list, k=int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = 0
#         while i < k:
#             self.oneRotate(nums)
#             i += 1

# Pass but take extra space
# can you solve it by O(1) space
class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        hold = nums + []
        for i in range(len(nums)):
            nums[(i + k) % len(nums)] = hold[i]
        return nums


s = Solution()
print(s.rotate(nums=[1], k=2))
print(s.rotate(nums=[1, 2], k=3))
print(s.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
