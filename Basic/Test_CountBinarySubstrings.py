# https://leetcode.com/problems/count-binary-substrings/

# !! Time limit Exceed

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # TODO init with 01 and 10
        # TODO check if in or not
        # TODO then increase 0 1

        count = 0

        init_1 = '01'
        while init_1 in s:
            count += s.count(init_1)
            init_1 = '0' + init_1 + '1'

        init_2 = '10'
        while init_2 in s:
            count += s.count(init_2)
            init_2 = '1' + init_2 + '0'

        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.countBinarySubstrings(s="00110011"))
    print(sol.countBinarySubstrings(s="10101"))
