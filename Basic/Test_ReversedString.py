def Solution(s=str):
    result = ''
    for i in reversed(range(len(s.split()))):
        if i != 0:
            result += s.split()[i] + ' '
        else:
            result += s.split()[i]
    return result


print(len(Solution('abc def ghijk ef' * 10 ** 3)))
