# https://leetcode.com/problems/goat-latin/

def Solution(S=str):
    Vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    output = ""
    CountA = 1
    Split = [i for i in S.split()]
    for i in range(len(Split)):
        plus = Split[i] + ''
        if Split[i][0] in Vowel:
            plus += 'ma'
        else:
            # remove the first letter
            first = plus[0]
            plus = plus[1:]
            plus += first + 'ma'
        plus += ('a' * CountA)
        output += plus
        if len(Split) != 1 and i != len(Split) - 1:
            output += ' '
        CountA += 1

    return output


print(Solution(S="I speak Goat Latin"))
# Imaa peaksmaaa oatGmaaaa atinLmaaaaa
print(Solution(S="The quick brown fox jumped over the lazy dog"))
print(len(Solution('THEEE' * 50)))
print(len(Solution("The quick brown fox jumped over the lazy dog" * 100)))
