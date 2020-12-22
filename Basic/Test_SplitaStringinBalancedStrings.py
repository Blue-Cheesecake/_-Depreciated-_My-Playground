# https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        balance = 0
        count = 0
        index = 0
        while index < len(s) - 1:
            found = False
            for i in range(index, len(s)):
                if s[i] == 'R':
                    balance += 1
                else:
                    balance -= 1
                if balance == 0:
                    count += 1
                    found = True
                    index = i + 1
                    break
            if not found:
                index += 1

        return count


if __name__ == "__main__":
    s = Solution()
    print(s.balancedStringSplit(s='RLLLLRRRLR'))
    # 3
    print(s.balancedStringSplit(s="RLRRLLRLRL"))
    # 4
    print(s.balancedStringSplit(s="LLLLRRRR"))
    # 1
    print(s.balancedStringSplit(s="RLRRRLLRLL"))
    # 2
