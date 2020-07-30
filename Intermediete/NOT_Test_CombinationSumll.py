def Solution(candidates=list, target=int):
    freq = {}
    for i in candidates:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
