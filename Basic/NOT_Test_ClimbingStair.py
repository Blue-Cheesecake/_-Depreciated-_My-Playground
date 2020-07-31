# https://leetcode.com/problems/climbing-stairs/

import itertools

# TLE And memory error


def Solution(n=int):
    ini = [1] * (n - 2)
    ini.append(2)
    # collapse 1 1 >> 2
    count = 0
    # even number is correct
    if n % 2 == 0:
        count += 2
        while ini.index(2) >= 2:
            count += len(set(list(itertools.permutations(ini))))
            cooldown = 0
            while 2 in ini:
                ini.remove(2)
                cooldown += 1
            ini.pop()
            ini.pop()
            while cooldown > -1:
                ini.append(2)
                cooldown -= 1
    else:
        count += 1
        while ini.index(2) != 1:
            count += len(set(list(itertools.permutations(ini))))
            cooldown = 0
            while 2 in ini:
                ini.remove(2)
                cooldown += 1
            ini.pop()
            ini.pop()
            while cooldown > -1:
                ini.append(2)
                cooldown -= 1

    return count

# odd number +1, even number + 2


print(Solution(5))
print(Solution(6))
print(Solution(7))
print(Solution(8))
print(Solution(12))
a = set(list(itertools.permutations([2, 1, 1, 1])))
b = set(list(itertools.permutations([2, 2, 1])))
print(a)
print(b)

# n = 6
# [1,1,1,1,1,1]
c = set(list(itertools.permutations([1, 1, 1, 1, 2])))
d = set(list(itertools.permutations([2, 2, 1, 1])))

print(len(c) + len(d) + 2)

# n = 7
e = set(list(itertools.permutations([2, 1, 1, 1, 1, 1])))
f = set(list(itertools.permutations([2, 2, 1, 1, 1])))
g = set(list(itertools.permutations([2, 2, 2, 1])))

print(len(e)+len(g)+len(f)+1)
