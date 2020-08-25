# https://leetcode.com/problems/valid-mountain-array/

def Solution(A=list):
    if len(A) >= 3:
        # increase and decrease can beused only one
        increase = False
        decrease = False
        # check if increase
        for i in range(len(A) - 1):
            if A[i] < A[i+1]:
                increase = True
            else:
                # break and go to check if decrease
                break
        for j in range(i, len(A) - 1):
            if A[j] > A[j+1]:
                decrease = True
            else:
                return False
        if increase and decrease:
            return True
    return False


# more optimal than above
def Solution2(A=list):
    N = len(A)
    i = 0

    # climb up
    while i+1 < N and A[i] < A[i+1]:
        i += 1
    # check if beginning or end
    if i == 0 or i == N-1:
        return False

    # check down
    while i+1 < N and A[i] > A[i+1]:
        i += 1

    # check index
    return i == N-1


print(Solution(A=[0, 2, 3, 4, 5, 2, 1, 0]))  # True
print(Solution(A=[2, 1]))  # False
print(Solution(A=[3, 5, 5]))  # False
print(Solution(A=[0, 3, 2, 1]))  # True
print(Solution(A=[55, 5, 5, 5]))  # False
print(Solution(A=[5, 5, 5, 5, 5]))  # False
print(Solution(A=[5, 6, 20, 6, 5]))  # True
print(Solution(A=[1, 2, 3, 4, 5, 5, 5, 5]))  # False
print(Solution(A=[5, 5, 5, 5, 4, 3, 2, 1]))  # False
print(Solution(A=[1, 3, 2]))  # True
