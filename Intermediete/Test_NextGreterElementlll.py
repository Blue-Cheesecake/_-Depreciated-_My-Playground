from itertools import permutations

n = 241
per = [''.join(i) for i in permutations(str(n))]
print(per)
exist = False
for j in range(len(per)):
    per[j] = int(per[j])
print(per)

sort = sorted(per)
sort.remove(n)
print(sort)

for k in sort:
    if k > n:
        exist = True
        print(k)
if not exist:
    print(-1)
