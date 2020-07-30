# output must be 1 1 4 1
# need test time (increase lim gradually)


def quadeq(given):
    mini = []
    lim = range(-50, 50)
    for a in range(50):
        for b in lim:
            for c in lim:
                for d in lim:
                    if a * c == given[0] and (a*d) + (b*c) == given[1] and b * d == given[2]:
                        mini.append(a)
                        if a <= mini[0]:
                            return a, b, c, d


test = [(6, -7, -5), (12, -31, 9), (12, -56, 9),
        (8, -26, 15), (1, 12, 4), (1, -25, -225)]

for x in test:
    try:
        i, j, k, l = quadeq(x)
    except:
        print('No solution')
    else:
        print(i, j, k, l)
