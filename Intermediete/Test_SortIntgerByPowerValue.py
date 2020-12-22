def NumStep(x):
    steps = [] + [x]
    while steps[-1] != 1:
        if steps[-1] % 2 == 0:
            element = steps[-1] // 2
            steps.append(element)
        else:
            element = 3 * steps[-1] + 1
            steps.append(element)
    return len(steps) - 1


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        DictList = []
        elem1 = list(range(lo, hi+1))
        elem2 = []

        for i in elem1:
            elem2.append(NumStep(i))

        for p, q in zip(elem1, elem2):
            DictList.append((p, q))

        sortDict = sorted(DictList, key=lambda kv: kv[1])

        return sortDict[k-1][0]
