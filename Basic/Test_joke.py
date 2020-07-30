st = ['ttt', 'a', 'g', 'v', 'h', 'ttt', 'f', 'h', 'h']


def find(iterab):
    ret = []
    for i in iterab:
        if i not in ret:
            ret.append(i)
    return ret


def find_2(iterab):
    return set(st)


print(find(st))
print(find_2(st))
