def Solution(n=int, k=int):
    facth = 0
    for i in range(1, n+1):
        if n % i == 0:
            facth += 1
        if facth == k:
            return i
    return -1


print(Solution(12, 3))
print(Solution(7, 2))
print(Solution(4, 4))
print(Solution(1000, 3))
print(Solution(1000, 16))
