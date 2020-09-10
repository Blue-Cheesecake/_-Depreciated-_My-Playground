# https://leetcode.com/problems/compare-version-numbers/

def Solution(version1=str, version2=str):
    v1 = version1.split(".")
    v2 = version2.split(".")
    # remove 0 before int
    for i in range(len(v1)):
        v1[i] = int(v1[i])
    for j in range(len(v2)):
        v2[j] = int(v2[j])
    # remove 0 from the last index
    if len(v1) != 1:
        i = len(v1) - 1
        while v1[i] == 0:
            v1.pop()
            i = len(v1) - 1
    if len(v2) != 1:
        i = len(v2) - 1
        while v2[i] == 0:
            v2.pop()
            i = len(v2) - 1
    i = 0
    try:
        while v1[i] == v2[i]:
            i += 1
    except IndexError:
        if len(v1) > len(v2):
            return 1
        elif len(v1) < len(v2):
            return -1
        else:
            return 0
    if v1[i] > v2[i]:
        return 1
    elif v1[i] < v2[i]:
        return -1
    else:
        return 0


print(Solution(version1='0', version2='1'))
