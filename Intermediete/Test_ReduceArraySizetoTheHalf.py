# https://leetcode.com/problems/reduce-array-size-to-the-half/

def Solution(arr=list):
    n = len(arr)
    atleast = n / 2
    freq = {}
    for i in arr:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    count = 0
    index = 0
    while n > atleast:
        n -= freq[index][1]
        count += 1
        index += 1
    return count


print(Solution(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
# 2
print(Solution(arr=[7, 7, 7, 7, 7, 7]))
# 1
print(Solution(arr=[1000, 1000, 3, 7]))
# 1
print(Solution(arr=[1, 9]))
# 1
