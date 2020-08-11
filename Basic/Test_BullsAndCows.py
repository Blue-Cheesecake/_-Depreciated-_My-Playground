# https://leetcode.com/problems/bulls-and-cows/

# if guess in secret : distinguish that is bull or cow
# A += 1 if guess is bull (element and index are equal each other)
# B += 1 if guess is cow (guess in secret but index arent equal and that secret havent used yet)
# problem is how to write code that element is used(counted)
# find used element and  do not use that elements again
# find bulls first


def BullsandCow(secret, guess):
    leftS = []
    leftG = []
    # find bulls
    A = 0
    for i, j in zip(enumerate(secret), enumerate(guess)):
        if i == j:
            A += 1
        else:
            leftS.append(i[1])
            leftG.append(j[1])
    # find cows
    B = 0
    for p in leftG:
        if p in leftS:
            # find index of p remove p in leftS
            leftS.pop(leftS.index(p))
            B += 1
        else:
            pass
    return str(A) + 'A' + str(B) + 'B'


# print(Solution('1123', '0111'))  # 1A1B
# print(Solution('11', '10'))  # 1A0B
# print(Solution('1807', '7810'))  # 1A3B
# print(Solution('1123', '0111'))  # 1A1B
# print(Solution('0111161', '1111102'))  # 4A2B
# print(Solution('1' * 10 ** 3, '1' * 10 ** 3))

print(BullsandCow('1123', '0111'))  # 1A1B
print(BullsandCow('11', '10'))  # 1A0B
print(BullsandCow('1807', '7810'))  # 1A3B
print(BullsandCow('1123', '0111'))  # 1A1B
print(BullsandCow('0111161', '1111102'))  # 4A2B
print(BullsandCow('1' * 10 ** 5, '1' * 10 ** 5))
