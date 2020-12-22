# https://leetcode.com/problems/climbing-stairs/

# odd number +1, even number + 2
# n! / n1!n2!


def factorial(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r


def Solution(n=int):
    ini = [1] * (n - 2)
    ini.append(2)
    result = 1
    setting = 1
    if n % 2 == 0:
        result = 2
        setting = 2
    try:
        while ini.index(2) >= setting:
            result += (factorial(len(ini)) //
                       (factorial(ini.count(1))*factorial(ini.count(2))))
            cooldown = 0
            while 2 in ini:
                ini.remove(2)
                cooldown += 1
            ini.pop()
            ini.pop()
            while cooldown > -1:
                ini.append(2)
                cooldown -= 1
    except:
        pass
    return result


for i in range(1, 46):
    print(Solution(i))

# print(factorial(4) / (factorial(3)))
# print(factorial(3) / factorial(2))
# a = set(list(itertools.permutations([2, 1, 1, 1])))
# b = set(list(itertools.permutations([2, 2, 1])))
# print(len(a) + len(b) + 1)

# # n = 6
# # [1,1,1,1,1,1]
# c = set(list(itertools.permutations([1, 1, 1, 1, 2])))
# d = set(list(itertools.permutations([2, 2, 1, 1])))

# print(len(c) + len(d) + 2)

# # n = 7
# e = set(list(itertools.permutations([2, 1, 1, 1, 1, 1])))
# f = set(list(itertools.permutations([2, 2, 1, 1, 1])))
# g = set(list(itertools.permutations([2, 2, 2, 1])))

# print(len(e)+len(g)+len(f)+1)
