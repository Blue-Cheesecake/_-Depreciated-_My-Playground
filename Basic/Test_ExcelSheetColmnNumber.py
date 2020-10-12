# https://leetcode.com/problems/excel-sheet-column-number/


def Solution(s=str):
    Reverse = s[::-1]
    Alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
                'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25 }
    output = 0
    if len(s) == 1:
        return Alphabet.get(s)
    else:
        for j in reversed(range(len(s))):
            output += 26 ** j * Alphabet.get(Reverse[j])
        return output


print(Solution('TEA'))
print(Solution('SET'))
print(Solution('TEA') - Solution('SET'))
# count = 0
# for i in range(1, 1400):
#     if 1400 % i == 0:
#         count += 1
# print(count)
