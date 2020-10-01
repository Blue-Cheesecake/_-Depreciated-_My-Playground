# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: list, arr2: list):
        # count freq
        freqNum = {}
        result = []
        for i in range(len(arr1)):
            if arr1[i] not in freqNum:
                freqNum[arr1[i]] = 1
            else:
                freqNum[arr1[i]] += 1
        for i in range(len(arr2)):
            j = 0
            while j < freqNum.get(arr2[i]):
                result.append(arr2[i])
                j += 1
            freqNum.pop(arr2[i])
        hold = []
        for i in freqNum.items():
            j = 0
            while j < i[1]:
                hold.append(i[0])
                j += 1
        return result + sorted(hold)


s = Solution()
print(s.relativeSortArray(
    arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
# [2,2,2,1,4,3,3,9,6,7,19]
