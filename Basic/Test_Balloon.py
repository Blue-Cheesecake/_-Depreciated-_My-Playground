# https://leetcode.com/problems/maximum-number-of-balloons/


def Solution(text):
    result = 0
    b = 0
    a = 0
    l = 0
    o = 0
    n = 0
    for i in text:
        if i == 'b':
            b += 1
        elif i == 'a':
            a += 1
        elif i == 'l':
            l += 1
        elif i == 'o':
            o += 1
        elif i == 'n':
            n += 1
    while True:
        if b >= 1 and a >= 1 and l >= 2 and o >= 2 and n >= 1:
            result += 1
            b -= 1
            a -= 1
            l -= 2
            o -= 2
            n -= 1
        else:
            break
    return result


print(Solution("nlaebolko"))
print(Solution("loonbalxballpoon"))
print(Solution("leetcode"))
print(Solution("ballonxxxxxxxballoonxxxxxxballoooonxxxxbalon"))
print(Solution('baloon'))
