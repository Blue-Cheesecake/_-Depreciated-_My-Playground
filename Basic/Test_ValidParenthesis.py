# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        # in case of no pairs
        if len(s) % 2 == 1:
            return False

        # access by index
        openP = ['(', '[', '{']
        closP = [')', ']', '}']

        if s[0] in closP:
            return False

        def checkindexOfMatch(oneS):
            if oneS == '(' or oneS == ')':
                return 0
            elif oneS == '[' or oneS == ']':
                return 1
            elif oneS == '{' or oneS == '}':
                return 2

        def validExpress(idxOfMain, s):
            oneS = s[idxOfMain]
            if oneS in openP:
                idxOfMain += 1
                # Max of s (no the next element)
                if idxOfMain >= len(s):
                    return False, s
                theNext = s[idxOfMain]
                if theNext in openP:
                    return idxOfMain, s
                else:
                    theNext = s[idxOfMain]
                    idx_Ma_Of_OneS = checkindexOfMatch(oneS)
                    idx_Ma_Of_Thenext = checkindexOfMatch(theNext)
                    if idx_Ma_Of_OneS == idx_Ma_Of_Thenext:
                        remove = oneS + theNext
                        s = s.replace(remove, '')
                        if idxOfMain > 1:
                            idxOfMain -= 2
                        else:
                            idxOfMain -= 1
                        if s == '':
                            return True, s
                        else:
                            return idxOfMain, s
                    else:
                        return False, s
            else:
                return False, s

        index = 0
        while s != '':
            result, s = validExpress(index, s)
            if isinstance(result, str) == True:
                pass
            elif isinstance(result, bool) == True:
                return result
            elif isinstance(result, int) == True:
                index = result

        return True

# credit --> someone in leetcode
# sry to copy this T_T
# because of just wanting to compare that my sol is very bad T_T


class Solution2:
    def isValid(self, s: str) -> bool:
        valid = False
        if s and len(s) > 1:
            stack = []
            char_set = ["{}", "()", "[]"]
            valid = True
            for char in s:
                if char in ["(", "{", "["]:
                    stack.append(char)
                elif char in [")", "}", "]"]:
                    if stack:
                        s_char = stack.pop()
                        if f"{s_char}{char}" not in char_set:
                            valid = False
                            break
                    else:
                        valid = False
                        break
            if stack:
                valid = False

        return valid


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(s='()[]'))
    # True
    print(sol.isValid(s="{[]}"))
    # True
    print(sol.isValid(s="{{}[][[[]]]}"))
    # # True
    print(sol.isValid(s="([)]"))
    # # False
    print(sol.isValid(s="(]"))
    # # False
    print(sol.isValid(s="[[[[(((())))]]]]"))
    # # True
    print(sol.isValid(s="([)]"))
    # # False
    print(sol.isValid(s="(("))
    # # False
    print(sol.isValid(s="()[][][]]"))
    # # False
    print(sol.isValid(s="]["))
    # # False
