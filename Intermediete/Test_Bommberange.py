def Solution(b=list):
    a = []
    m1 = None
    m2 = None
    m3 = None
    for i in b:
        if i not in a:
            a.append(i)
    if len(a) == 3:
        try:
            m1 = abs(a[0][1] - a[1][1]) / abs(a[0][0] - a[1][0])
        except:
            m1 = 'undefined'
        try:
            m2 = abs(a[0][1] - a[2][1]) / abs(a[0][0] - a[2][0])
        except:
            m2 = 'undefined'
        try:
            m3 = abs(a[1][1] - a[2][1]) / abs(a[1][0] - a[2][0])
        except:
            m3 = 'undefined'
        if m1 != m2 or m1 != m3 or m2 != m3:
            return True
        else:
            return False
    else:
        return False


# 0 1, 0 2, 1 2
print(Solution([[1, 1], [2, 3], [3, 2]]))
print(Solution([[1, 1], [2, 2], [3, 3]]))
print(Solution([[0, 0], [0, 2], [2, 1]]))
print(Solution([[0, 1], [0, 1], [2, 1]]))
