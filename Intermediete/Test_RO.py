# โจทย์โดย : สรวิทย์  สุริยกาญจน์ ( PS.int )
# ที่มา : ศูนย์ สอวน. โรงเรียนมหิดลวิทยานุสรณ์
# 15 3 where 15 = n , 3 = k
# RORROOROOROOORO = state
# output must be 8
n = 17
k = 3
state = 'OROOOOOROOOOORRRR'
numso = 0
for i in range(len(state)):
    if state[i] == 'O':
        numso += 1
divide = int(numso / k)
time = 1
time2 = 1
divides = divide * time
computeN = (divide * time) + time2
reststate = ''
restlist = []
while divides <= numso:
    for i in range(len(state)):
        reststate += state[i]
        if len(reststate) == computeN:
            O = 0
            for j in reststate:
                if j == 'O':
                    O += 1
            if O == divides:
                restlist.append(reststate)
                reststate = ''
                time += 1
                time2 += 1
                divides = divide * time
                computeN = divides + time2
                break
            else:
                O = 0
                reststate = reststate[1:computeN]
longest = 0
if len(restlist) != 0:
    for i in range(len(restlist)):
        exa = len(restlist[i])
        if exa > longest:
            longest = exa
else:
    longest = -1
print(longest)

# solved by Sinut Wattanarporn
