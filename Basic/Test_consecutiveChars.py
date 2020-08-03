# https://leetcode.com/problems/consecutive-characters/


def Solution(s=str):
    if len(s) != 1:
        maxi = 0
        ini = 0
        while ini < len(s) - 1:
            compare = ''
            compare += s[ini]
            for i in range(ini+1, len(s)):
                if s[i] == compare[len(compare) - 1]:
                    compare += s[i]
                if s[i] != compare[len(compare) - 1] or i == len(s) - 1:
                    maxi = max(len(compare), maxi)
                    ini += 1
                    break
    else:
        return 1
    return maxi


print(Solution(s='leetcode'))
print(Solution(s="abbcccddddeeeeedcba"))
print(Solution(s="triplepillooooow"))
print(Solution(s="hooraaaaaaaaaaay"))
print(Solution(s="tourist"))
print(Solution(s="eaedefegehejeleppppp"))
print(Solution('rrsr'*125))
