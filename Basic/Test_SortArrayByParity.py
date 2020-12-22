# https://leetcode.com/problems/sort-array-by-parity/

# find even and odd separately [even] [odd]
# merge it together +
def Solution(A=list):
    even = []
    odd = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd


print(Solution(A=[3, 1, 2, 4] * 250))
