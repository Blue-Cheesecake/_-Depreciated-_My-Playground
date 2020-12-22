# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(" ")

        def checkIfNull(index, a):
            if index < 0:
                return 0
            if a[index] == "":
                return checkIfNull(index - 1, a)
            else:
                return len(a[index])

        return checkIfNull(len(a) - 1, a)


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord(s="Hello World"))
    print(s.lengthOfLastWord(s="a   "))
    print(s.lengthOfLastWord(s="   "))
