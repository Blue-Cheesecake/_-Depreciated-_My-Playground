def looblike(iterab):
    dic = {}
    for i in iterab:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    sort = sorted(dic.items(), key=lambda kv: kv[1], reverse=True)
    ret = []
    most = 0
    for j in sort:
        if j[1] >= most:
            most = j[1]
            ret.append(j[0])
        else:
            pass
    return ret


test = (1, 1, 1, 3, 3, 6, 6, 7, 8)
test2 = (4, 3, 9, 8, 3, 3, 8)
test3 = (12, 2, 1, 12, 1, 1, 12)
print(looblike(test))
print(looblike(test2))
print(looblike(test3))
