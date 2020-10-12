# https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: list, n: int) -> list:
        result = []
        init = 0
        for i in range(1, n+1):
            if i == target[init]:
                result.append("Push")
                init += 1
            else:
                result.extend(["Push", "Pop"])
            if init == len(target):
                break
        return result


s = Solution()
print(s.buildArray(target=[1, 3], n=3))
print(s.buildArray(target=[1, 2, 3], n=3))
print(s.buildArray(target=[1, 2], n=4))
print(s.buildArray(target=[2, 3, 4], n=4))
