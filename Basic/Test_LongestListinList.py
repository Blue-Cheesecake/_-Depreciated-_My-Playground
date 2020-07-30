# find a number of the longest list in list


def Solution(n):
    if n < 10 and n >= 0:
        return n
    else:
        groups = []
        sigma = 0
        for i in range(1, n+1):
            new = True
            for j in repr(i):
                sigma += int(j)
            if len(groups) != 0:
                for k in groups:
                    if sigma == k[0]:
                        k.append(i)
                        sigma = 0
                        new = False
                        break
                if new:
                    groups.append([i])
                    sigma = 0
                    new = True
            else:
                groups.append([sigma])
                sigma = 0
    return max(len(ele) for ele in groups)


print(Solution(3))
print(Solution(15))
print(Solution(24))
print(Solution(13))
print(Solution(10))
print(Solution(100))
print(Solution(1000))
print(Solution(10000))
