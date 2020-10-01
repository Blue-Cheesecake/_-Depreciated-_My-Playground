# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        Dynamic = [0, 1, 1]
        for i in range(n + 1):
            if n <= len(Dynamic) - 1:
                return Dynamic[n]
            Dynamic.append(Dynamic[i]+Dynamic[i + 1]+Dynamic[i+2])


s = Solution()
print(s.tribonacci(4))
for i in range(10):
    print(s.tribonacci(i))
