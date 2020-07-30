# turn on the light in step x
# check if they can be blue
# they can be blue if all previous x turned on
# TLE becuase 0 for loop : find the another ways
# >>> how to know if each i bulb turned on <<<


def Bubba(light=list):
    On = [0 for i in light]
    count = 0
    Max = 0
    for i in light:
        On[i - 1] = i
        Max = max(Max, i)
        if 0 not in On[:Max]:
            count += 1
    return count


print(Bubba([3, 2, 4, 1, 5]))  # 2
print(Bubba([2, 1, 3, 5, 4]))  # 3
print(Bubba([4, 1, 2, 3]))  # 1
print(Bubba([2, 1, 4, 3, 6, 5]))  # 3
print(Bubba([1, 2, 3, 4, 5, 6]))  # 6
print(Bubba(list(range(5 * 10 ** 2))))
print(Bubba(list(range(5 * 10 ** 3))))
# print(Bubba(list(range(5 * 10 ** 4))))
