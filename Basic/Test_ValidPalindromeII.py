# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # TODO delete 1 to n char
        # TODO reverse and check if it palindrome or not
        for i in range(len(s)):
            origin = s[:i] + s[i + 1:]
            rev = origin[::-1]

            if origin == rev:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.validPalindrome("aba"))
    # ! True
    print(s.validPalindrome("abca"))
    # ! True
    print(s.validPalindrome("efg"))
