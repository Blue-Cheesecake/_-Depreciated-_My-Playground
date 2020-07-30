li = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
i = 0
suspect = 5
while i <= len(li):
    if suspect in li[i]:
        print(i)
        break
    i += 1
