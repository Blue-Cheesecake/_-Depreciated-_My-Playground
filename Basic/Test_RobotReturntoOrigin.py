# https://leetcode.com/problems/robot-return-to-origin/
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ver = 0
        hor = 0

        for i in range(len(moves)):
            if moves[i] == 'U':
                ver += 1
            elif moves[i] == 'D':
                ver -= 1
            elif moves[i] == 'R':
                hor += 1
            elif moves[i] == 'L':
                hor -= 1

        if ver == 0 and hor == 0:
            return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.judgeCircle(moves="UD"))
    # ! True
    print(sol.judgeCircle(moves="LL"))
    # ! false
    print(sol.judgeCircle(moves="RRDD"))
    # ! false
    print(sol.judgeCircle(moves="LDRRLRUULR"))
    # ! false
    print(sol.judgeCircle(moves="UUDDLLRR"))
