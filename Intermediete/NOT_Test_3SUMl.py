def Solution(nums=list):
    freq = {}
    for i in freq:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    freq = sorted(freq.items(), key=lambda kv: kv[0])
    result = []
    indx = 0
    while indx < len(freq) - 3:
        const = 1
        if freq[indx][1] > 0:
            x = freq[indx][0]
            for l in freq[indx+const:len(freq) - 2]:
                if l[1] > 0:
                    y = l[0]
                    z = -x - z
                    if z in nums:
                        result.append([x, y, z])
                        freq[indx][1] -= 1
                        l[1] -= 1
