# https://leetcode.com/problems/adding-two-negabinary-numbers/


# turn list --> number --> plus --> binary
def plus(arr):
    arr = arr[::-1]
    out = 0
    for i in reversed(range(len(arr))):
        if arr[i] == 1:
            out += ((-2) ** i)
    return out


def Solution(arr1=list, arr2=list):
    ret = []
    a = bin(plus(arr1) + plus(arr2))
    for i in a:
        ret.append(int(i))
    return ret


print(Solution([1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], [1, 0, 1]))
