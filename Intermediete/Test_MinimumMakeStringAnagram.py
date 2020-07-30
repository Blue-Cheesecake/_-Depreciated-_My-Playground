def frequency(lists):
    freq = {}
    for i in lists:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    return freq


def Solution(s=str, t=str):
    freqS = frequency(s)
    freqT = frequency(t)
    freqS = sorted(freqS.items(), key=lambda kv: kv[0])
    freqT = sorted(freqT.items(), key=lambda kv: kv[0])
    count = 0
    for i in freqT:
        if i[0] not in s:
            count += i[1]
        else:
            # if i[0] value more than original, count += 1
            # indx is i[0] in freqS
            indx = 0
            while indx <= len(freqS):
                if i[0] in freqS[indx]:
                    break
                indx += 1
            if i[1] > freqS[indx][1]:
                count += i[1] - freqS[indx][1]
    return count


print(Solution(s="bab", t="aba"))
print(Solution(s="leetcode", t="practice"))
print(Solution(s="anagram", t="mangaar"))
print(Solution(s="xxyyzz", t="xxyyzz"))
print(Solution(s="friend", t="family"))
print(Solution(s="y"*1000, t="x"*1000))
print(Solution("gctcxyuluxjuxnsvmomavutrrfb", "qijrjrhqqjxjtprybrzpyfyqtzf"))
