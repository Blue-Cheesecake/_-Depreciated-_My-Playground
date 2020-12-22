# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # turn into array
        arr = [S[i] for i in range(len(S))]
        holdS = ''
        staticIndex = 0
        # checkLoop = staticIndex + 0
        while staticIndex < len(arr):
            stack = 0
            for i in range(staticIndex, len(arr)):
                if arr[i] == '(':
                    stack += 1
                else:
                    stack -= 1
                    if stack == 0:
                        break
            for j in range(staticIndex + 1, i):
                holdS += arr[j]
            staticIndex = i + 1

        return holdS


S = Solution()
# print(S.removeOuterParentheses("(()())(())"))
# print(S.removeOuterParentheses("()()"))
print(S.removeOuterParentheses("(()())(())(()(()))"))
