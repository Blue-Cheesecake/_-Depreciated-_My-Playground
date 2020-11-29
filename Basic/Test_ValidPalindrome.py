# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                temp += s[i].lower()
        palindrome = temp[::-1]
        if temp == palindrome:
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(s="A man, a plan, a canal: Panama"))
    # True
    print(s.isPalindrome(s="race a car"))
