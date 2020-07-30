# binary search


def xk(given):
    for i in given:
        most_val = 0
        for x in range(2, 1000):
            for k in range(2, 20):
                if x ** k == i:
                    if k >= most_val:
                        most_val = k
        if most_val == 0:
            yield 'No'
        else:
            yield most_val


given = (1000000, 994009, 20, 59050, 524288)
for A in xk(given):
    print(A)
