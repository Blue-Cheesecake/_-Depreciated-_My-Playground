def ttP(cy: tuple, n: int):
    a = [i for i in range(1, n + 1)]
    for i in range(len(cy)):
        each = cy[i]
        if i != len(cy) - 1:
            index = cy[i+1]
            a[each - 1] = a[index - 1]
        else:
            a[each - 1] = cy[0]

    return a
    

class P:

    def __init__(self, p: list):
        self.p = p

    def rev(self):
        # ! index of i + 1
        hold = []
        for i in range(1, len(self.p) + 1):
            hold.append(self.p.index(i) + 1)

        self.p = hold

    def comp(self, p1, p2):
        hold = []
        for i in range(len(p1.p)):
            element = p2.p[i]
            actual_index = element - 1
            app = p1.p[actual_index]
            hold.append(app)
        self.p = hold

    def multiComp(self, cys, n):
        # ! turn cy into permutation
        p1 = P(ttP(cys[0], n))
        p2 = P(ttP(cys[1], n))
        main = P([])
        main.comp(p1, p2)

        if len(cys) > 2:
            for i in range(2, len(cys)):
                each = cys[i]
                another = P(ttP(each, n))
                main.comp(main, another)

        self.p = main.p

    def pp(self):
        print(self.p)


def codeMassage(word: str, p: P([])):
    di = []
    for i in range(len(p.p)):
        di.append((word[i], p.p[i]))
    di = sorted(di, key=lambda kv: kv[1])
    after = ""
    for i in range(len(di)):
        after += di[i][0]
    return after


def deCodeMassage(word: str, p: P([])):
    before = ""
    for i in range(len(p.p)):
        before += word[p.p[i] - 1]
    return before


if __name__ == "__main__":

    # p5 = P(ttP((6, 8), 8))
    # p6 = P(ttP((2, 3), 8))
    # p7 = P(ttP((1, 4, 5), 8))
    # p8 = P([])
    # p8.comp(p5, p6)
    # p9 = P([])
    # p9.comp(p8, p7)
    # p9.pP()

    # ! multi composition
    # p10 = P([])
    # p10.multiComp((((3, 6), (3, 1), (4, 5), (4, 2), (4, 8))), 8)
    # p10.pp()
    # p11 = P([])
    # p11.multiComp(((5, 7, 8, 6), (1, 2, 3, 4)), 8)
    # p11.pp()
    # p12 = P([])
    # p12.multiComp(((1, 2, 4), (3, 5, 6)), 6)
    # # p12.rev()
    # p12.comp(p12, p12)
    # p12.pp()

    # ! encode massage
    # p1 = P([])
    # p1.multiComp(((1, 3, 5, 7, 9, 11), (2, 4, 6, 8, 10)), 11)
    # p1.pp()
    # after = codeMassage("WHEREAREYOU", p1)
    # print(after)

    # ! decode massage
    # p1 = P([])
    # p1.multiComp(((11, 9, 7, 5, 3, 1), (2, 4, 6, 8, 10, 12)), 12)
    # p1.pp()
    # b = deCodeMassage("TELNIEELCGIN", p1)
    # print(b)

    p1 = P([3, 4, 1, 2, 6, 5])
    p2 = P([2, 3, 1, 5, 4, 6])
    p3 = P([6, 3, 2, 5, 4, 1])
    p3.rev()
    p2.rev()
    p3.comp(p3, p2)
    # p1.comp(p1, p2)
    # p1.comp(p1, p3)
    # p1.pp()

    pass
    