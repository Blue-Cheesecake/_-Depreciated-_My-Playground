# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # TODO store alphabet --> reverse
        # TODO replace alphabet

        hold = ""
        for i in range(len(S)):
            if S[i].isalpha():
                hold += S[i]

        hold = hold[::-1]

        result = ""
        index_hold = 0
        for i in range(len(S)):
            if S[i].isalpha():
                result += hold[index_hold]
                index_hold += 1
            else:
                result += S[i]

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseOnlyLetters("ab-cd"))
    print(sol.reverseOnlyLetters("a-bC-dEf-ghIj"))
    print(sol.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
