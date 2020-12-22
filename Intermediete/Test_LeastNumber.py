def Solution(arr=list, k=int):
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    order = sorted(freq.items(), key=lambda kv: kv[1])
    output = 0
    end = False
    for i in range(len(order)):
        item = list(order[i])
        while item[1] > 0:
            if k > 0:
                item[1] -= 1
                k -= 1
            else:
                output = len(order[i:])
                end = True
                break
        if end:
            break

    return output


print(Solution(arr=[5, 5, 4], k=1))
print(Solution(arr=[4, 3, 1, 1, 3, 3, 2], k=3))
print(Solution(arr=list(range(10000)), k=9999))
print(Solution(arr=[2, 1, 1, 3, 3, 3], k=3))
