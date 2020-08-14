# power set

p = [1, 2, 3, 4, 5, 6]


def powerset(sets):
    result = [[]]
    for i in sets:
        arry = [subset + [i] for subset in result]
        result.extend(arry)
    return result

# another way


def powerset_2(sets):
    result = [[]]
    for i in sets:
        arry = []
        for subset in result:
            arry.append(subset + [i])
        for ar in arry:
            result.append(ar)
    return result


print(powerset([1, 2, 3]))
print(len(powerset(p)))
print(1/len(powerset(p)) * 100)
