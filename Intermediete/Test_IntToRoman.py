class Solution:

    def intToRoman(self, num: int) -> str:

        def helper(n, pos) -> str:

            index = 0

            if pos == 2:
                index = 2
            elif pos == 3:
                index = 4
            elif pos == 4:
                index = 6

            roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

            # ! pattern of each digit
            if n <= 3:
                return roman[index] * n
            elif n == 4:
                return roman[index] + roman[index + 1]
            elif n <= 8:
                return roman[index + 1] + (roman[index] * (n - 5))
            elif n == 9:
                return roman[index] + roman[index + 2]
            return ""

        result = ""
        r = str(num)
        pos = len(r)

        for digit in r:
            result += helper(int(digit), pos)
            pos -= 1

        return result


if __name__ == "__main__":
    r = Solution()
    print(r.intToRoman(1994))
