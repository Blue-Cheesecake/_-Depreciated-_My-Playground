# https://leetcode.com/problems/power-of-two/


def Solution(n=int):
    if n < 0:
        return False
    BiValue = bin(n)
    return BiValue.count('1') == 1


for i in range(1, 10):
    print(Solution(2 * i))
