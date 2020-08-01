import sys
INT_MAX = sys.maxsize


def Solution(n):
    if n <= INT_MAX:
        count = 0
        left = n
        for expect in range(1, n+1):
            left = left - expect
            if left >= 0:
                count += 1
            else:
                break
    return count


print(INT_MAX)
print(Solution(5))
print(Solution(10))
