# len(digits) -1 += 1
# if that num == 9 >> len(digits) - 1 - 1 += 1 that indx of num = 0
# reverse range len list if i == 9 digits i = 0 plus = True
# helper loop untill the next num != 9


def Solution(digits=list):
    i = len(digits) - 1
    if digits[i] != 9:
        digits[i] += 1
    else:
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
            if digits[i] != 9:
                if i != -1:
                    digits[i] += 1
                else:
                    digits.insert(0, 1)
                break
    return digits


print(Solution([1, 2, 3, 4, 5]))
print(Solution([1, 2, 3, 4, 9]))
print(Solution([9]))
print(Solution([1, 2, 3, 4, 9, 9]))
