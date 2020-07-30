def powerset(sets):
    result = [[]]
    for i in sets:
        arry = [subset + [i] for subset in result]
        result.extend(arry)
    return result


def ret(ele):
    for i in range(len(ele)):
        if len(ele[i]) == 7:
            yield ele[i]


def sanowhite(li):
    for j in ret(powerset(li)):
        if sum(j) == 100:
            return j


li = [7, 8, 10, 13, 15, 19, 20, 23, 25]
li2 = [8, 6, 5, 1, 37, 30, 28, 22, 36]
print(sanowhite(li))
print(sanowhite(li2))
