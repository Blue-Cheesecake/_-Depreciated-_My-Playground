command = ('ABCDEF', 'AAABBBBCDE', 'CCCCCADDCA')
point = {}
for i in range(len(command)):
    for j in command[i]:
        if j not in point:
            point[j] = 1
        else:
            point[j] += 1
    sort_point = sorted(point.items(), key=lambda kv: kv[1])
    if sort_point[0][1] == sort_point[1][1]:
        pass
    else:
        key = sort_point[0][0]
        del point[key]

sort = sorted(point.items(), key=lambda kv: kv[1], reverse=True)
print(len(sort))
print(sort)
