# https://leetcode.com/problems/top-k-frequent-elements/


def Solution(nums=list, k=int):
    freq = {}
    for i in nums:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    result = []
    for j in range(k):
        result.append(freq[j][0])
    return result


print(Solution([1, 1, 1, 2, 2, 3], 2))
