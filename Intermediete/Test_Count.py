def rotated(lst):
    last = lst[0]
    arry = lst
    for i in range(len(lst)):
        try:
            arry[i] = lst[i+1]
        except IndexError:
            arry[len(lst) - 1] = last
    return arry


def sets(lst):
    var = []
    for i in lst:
        if i not in var:
            var.append(i)
    return var


given_n = 5
given_k = 4
ranger = list(range(1, given_n+1))
count = 0
while len(ranger) != 1:
    for i in range(len(ranger)):
        count += 1
        if count == given_k:
            given_k = ranger[i]
            try:
                var = ranger[i+1]
            except IndexError:
                ranger = ranger + [p for p in ranger]
                var = ranger[i+1]
            for r in ranger:
                if r == given_k:
                    ranger.remove(given_k)
            while ranger.index(var) != 0:
                ranger = rotated(ranger)
            ranger = sets(ranger)
            count = 0
            break
        else:
            if given_k > len(ranger):
                ranger = ranger + [p for p in ranger]
                count = 0
                break


print(ranger)

# solved by Sinut Wattanarporn
