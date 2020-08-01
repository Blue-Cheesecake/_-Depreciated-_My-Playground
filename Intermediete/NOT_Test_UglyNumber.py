def findPrimeFactors(num=int):
    for i in range(2, num+1):
        if num != 1:
            if num % i == 0:
                if i == 2 or i == 3 or i == 5:
                    while num % i == 0:
                        num /= i
                else:
                    return False
        else:
            break
    return True


# another make TLE

def another(num):
    only = [2, 3, 5]
    for i in only:
        while num % i == 0:
            num /= i
    if num != 1:
        return False
    return True


# Most number are not ugly, try to generate only ugly numbers

def Solution(n=int):
    L1 = 2
    L2 = 3
    L3 = 5
    # try to not using list
    result = 0
    count = 1
    while True:
        minimum = min(L1, L2, L3)
        if another(minimum):
            result = max(result, minimum)
            count += 1
            if count == n:
                return result
        if L1 == minimum:
            L1 += 2
        if L2 == minimum:
            L2 += 3
        if L3 == minimum:
            L3 += 5


print(Solution(10))
print(Solution(5))
print(Solution(125))
print(Solution(350))
print(Solution(450))
