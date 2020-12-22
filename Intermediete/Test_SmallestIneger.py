def Solution(k):
    n = 1
    if k % 2 == 0 or k % 5 == 0:
        return -1
    while True:
        if int(n) % k == 0:
            break
        else:
            n = n * 10 + 1
    return (len(str(n)))


print(Solution(2))
print(Solution(29))
print(Solution(3))
print(Solution(5367))
print(Solution(149))
print(Solution(19927))
