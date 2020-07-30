# output must be 'ACTGCTA'
def findDNA(dna1, dna2):
    if len(dna1) > len(dna2):
        dna1, dna2 = dna2, dna1
    room = []
    for i in range(len(dna1)):
        for j in range(len(dna1)):
            if dna1[i] == dna2[j]:
                state = ''
                state += dna1[i]
                k = i + 1
                l = j + 1
                while l != len(dna2):
                    for r, s in zip(range(k, len(dna1)), range(l, len(dna2))):
                        if dna1[r] == dna2[s]:
                            state += dna1[r]
                            k += 1
                            l += 1
                        else:
                            break
                    break

                room.append(state)
    return room


Dna_1 = 'AAAACTGCTACCGGTLMNOPQRST'
Dna_2 = 'CTGAATCTACTLMNAOPQRSTGCTATTGCAA'


rest = findDNA(Dna_1, Dna_2)
longest = 0
result = ''
for i in rest:
    measure = len(i)
    if measure > longest:
        longest = measure
        result = i
print(result)
print(rest)

# solved by Sinut Wattanarporn
