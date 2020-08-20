# https://leetcode.com/problems/squares-of-a-sorted-array/

# power it and sort them
def Solution(A=list):
    for i in range(len(A)):
        A[i] = A[i] ** 2
    A.sort()
    return A


print(Solution(A=[-4, -1, 0, 3, 10]))
# [0,1,9,16,100]
print(Solution(A=[-7, -3, 2, 3, 11]))
# [4,9,9,49,121]
print(len(Solution(A=[10000] * 100000)))
