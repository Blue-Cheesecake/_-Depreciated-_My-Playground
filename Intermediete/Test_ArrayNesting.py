# https://leetcode.com/problems/array-nesting/


# Time limit Exceed
class Solution:
    def arrayNesting(self, nums: list) -> int:
        maci = 0
        for i in range(len(nums)):
            index = i + 0
            S = []
            # False = 0
            # True = 1
            duplitcate = False
            while not duplitcate:
                if nums[index] in S:
                    duplitcate = True
                else:
                    S.append(nums[index])
                    index = nums[index]
            maci = max(maci, len(S))
        return maci

    def arrayNesting2(self, nums: list) -> int:
        maci = 0
        for i in range(len(nums)):
            index = i + 0
            hold = nums + []
            size = 0
            duplitcate = False
            while not duplitcate:
                if nums[index] not in hold:
                    duplitcate = True
                else:
                    hold.remove(nums[index])
                    index = nums[index]
                    size += 1
            maci = max(maci, size)
        return maci


s = Solution()

print(s.arrayNesting(nums=[5, 4, 0, 3, 1, 6, 2]))
# 4
