# https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count

# n * (n – 1) // 2


class Solution2:
    def numIdenticalPairs(self, nums: list) -> int:
        freq = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        for i in freq.keys():
            count += (freq.get(i) * (freq.get(i) - 1) // 2)
        return count
