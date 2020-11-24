# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        # if the next symbol is greater than previous then its 4 or 9
        result = 0
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i = 0
        pass_the_next_i = False
        while i < len(s):
            if pass_the_next_i:
                i += 1
                pass_the_next_i = False
                continue
            temp = val.get(s[i])
            comp = 0
            if i + 1 < len(s):
                comp = val.get(s[i+1])
            if comp != 0:
                if temp < comp:
                    temp = comp - temp
                    pass_the_next_i = True
            else:
                pass_the_next_i = False

            i += 1
            result += temp

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt(s="IX"))
    # 9
    print(s.romanToInt(s="LVIII"))
    # 58
    print(s.romanToInt(s="MCMXCIV"))
    # 1994
    print(s.romanToInt(s="XIV"))
    # 14
