# 1 <= n <= 500


def Solution(n=int):
    result = ''
    if n >= 2:
        if (n - 1) % 2 != 0:
            result += 'a' * (n - 1)
            result += 'b' * (n - (n-1))
        else:
            result += 'a' * (n - 2)
            result += 'b'
            result += 'c'
    else:
        if n == 1:
            return 'a'
        else:
            return 'ab'

    return result


print(Solution(8))
print(Solution(7))
print(Solution(1))
print(Solution(2))
print(Solution(3))
print(Solution(4))
