# https://leetcode.com/problems/largest-time-for-given-digits/


def Solution(arr=list):
    # pq:rs
    # p : 0 1 2
    # q : 0 1 2 3
    # r : 0 1 2 3 4 5
    # s : 0 1 2 3 4 5 6 7 8 9
    # if 6 or more than 6 appear 2 times:
    # assigh max(6-9 1,6-9 2) = q and s
    p = ''
    q = ''
    r = ''
    s = ''
    settingi = 3
    settingj = 4
    settingk = 6
    settingl = 10
    hold = arr + []
    find = range(6, 10)
    count = 2
    appear2times = 0
    while count != 0:
        for f in find:
            if f in hold:
                appear2times += 1
                hold.remove(f)
        count -= 1
    if appear2times == 2:
        settingi = 2
    for i in reversed(range(settingi)):
        if i in arr:
            p += str(i)
            arr.remove(i)
            break
    # q in range(10)
    if p == '0' or p == '1':
        settingj = 10
    for j in reversed(range(settingj)):
        if j in arr:
            q += str(j)
            arr.remove(j)
            break
    for k in reversed(range(settingk)):
        if k in arr:
            r += str(k)
            arr.remove(k)
            break
    for l in reversed(range(settingl)):
        if l in arr:
            s += str(l)
            arr.remove(l)
            break
    if len(arr) >= 1:
        return ""
    return p + q + ':' + r + s


print(Solution([1, 2, 3, 4]))
# 23:41
print(Solution([5, 5, 5, 5]))
# ""
print(Solution([0, 0, 0, 0]))
# 00:00
print(Solution([0, 0, 1, 0]))
# 10:00
print(Solution([0, 4, 0, 0]))
# 04:00
print(Solution([4, 1, 0, 0]))
# 14:00
print(Solution([2, 0, 6, 6]))
# 06:26
