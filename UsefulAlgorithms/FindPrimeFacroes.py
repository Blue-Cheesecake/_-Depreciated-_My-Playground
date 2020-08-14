def findPrimeFactors(num=int):
    left = num + 0
    factors = []
    for i in range(2, num):
        if left != 1:
            if left % i == 0:
                while left % i == 0:
                    factors.append(i)
                    left /= i
        else:
            break
    return factors


print(findPrimeFactors(126))
