# Initilize the minimum or maximum value
import sys
INT_MIN = -sys.maxsize - 1
INT_MAX = sys.maxsize
# Returns maximum sum in a
# subarray of size k.


def maxSum(arr, n, k):

    # Initialize result
    max_sum = INT_MIN

    # Consider all blocks
    # starting with i.
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]

        # Update result if required.
        max_sum = max(current_sum, max_sum)

    return max_sum


def minSum(arr, n, k):

    # Initialize result
    min_sum = INT_MAX

    # Consider all blocks
    # starting with i.
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]

        # Update result if required.
        min_sum = min(current_sum, min_sum)

    return min_sum


arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
k = 2
n = len(arr)
print(maxSum(arr, n, k))
print(minSum(arr, n, k))
