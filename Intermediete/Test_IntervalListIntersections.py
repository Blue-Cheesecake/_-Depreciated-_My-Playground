# https://leetcode.com/problems/interval-list-intersections/

def Solution(A=list, B=list):
    # find intersection
    # find min max of A[i][j] comparing to B[i][j]
    # left --> find maximum
    # right --> find minimum
    # check if left and right is in A[i] and B[i]
    indexA = 0
    # compare index A to whole B , if B[i][0] > A[j][1] break
    result = []
    while indexA < len(A):
        indexB = 0
        while indexB < len(B):
            if B[indexB][0] <= A[indexA][1]:
                left = max(A[indexA][0], B[indexB][0])
                right = min(A[indexA][1], B[indexB][1])
                # can optimize by using binarysearch
                if left in range(B[indexB][0], B[indexB][1] + 1) and right in range(A[indexA][0], A[indexA][1] + 1):
                    result.append([left, right])
            else:
                break
            indexB += 1
        indexA += 1
    return result


print(Solution(A=[[0, 5]], B=[[1, 7]]))
# [1,5]
print(Solution(A=[[0, 2], [5, 10], [13, 23], [24, 25]],
               B=[[1, 5], [8, 12], [15, 24], [25, 26]]))
print(Solution(A=[[1, 5], [8, 12], [15, 24], [25, 26]],
               B=[[0, 2], [5, 10], [13, 23], [24, 25]]))
