# cal the outside first that each char are equals or less than n/4
def Solution(string):
    eachChar = len(string) // 4
    result = 4
    for i in range(len(string) - 4 + 1):
        continueous = True
        Q = 0
        W = 0
        E = 0
        R = 0
        count = 0
        # calculate outside 2-pointer
        for l in range(i+4, len(string)):
            if string[l] == 'Q':
                if Q < eachChar:
                    Q += 1
                else:
                    continueous = False
                    break
            elif string[l] == 'W':
                if W < eachChar:
                    W += 1
                else:
                    continueous = False
                    break
            elif string[l] == 'E':
                if E < eachChar:
                    E += 1
                else:
                    continueous = False
                    break
            elif string[l] == 'R':
                if R < eachChar:
                    R += 1
                else:
                    continueous = False
                    break
        if i >= 1 and continueous:
            # calculate outside 2-pointer
            for m in range(i):
                if string[m] == 'Q':
                    if Q < eachChar:
                        Q += 1
                    else:
                        continueous = False
                        break
                elif string[m] == 'W':
                    if W < eachChar:
                        W += 1
                    else:
                        continueous = False
                        break
                elif string[m] == 'E':
                    if E < eachChar:
                        E += 1
                    else:
                        continueous = False
                        break
                elif string[m] == 'R':
                    if R < eachChar:
                        R += 1
                    else:
                        continueous = False
                        break

        # inside 2-pointer
        if continueous:
            # find the first and last string that be replaced
            # return the length of substr from first and last that were replaced
            for j in range(i, i+4):
                if string[j] == 'Q':
                    if Q >= eachChar:
                        rev = string[j::]
                        rev = rev[:: -1]
                        for ele in range(len(rev[len(string) - j + 1])):
                            if rev[ele] == 'Q' and Q >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'W' and W >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'E' and E >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'R' and R >= eachChar:
                                count = len(rev[ele])
                    else:
                        Q += 1
                elif string[j] == 'W':
                    if W >= eachChar:
                        rev = string[j::]
                        rev = rev[:: -1]
                        for ele in range(len(rev[len(string) - j + 1])):
                            if rev[ele] == 'Q' and Q >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'W' and W >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'E' and E >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'R' and R >= eachChar:
                                count = len(rev[ele])
                    else:
                        W += 1
                elif string[j] == 'E':
                    if E >= eachChar:
                        rev = string[j::]
                        rev = rev[:: -1]
                        for ele in range(len(rev[len(string) - j + 1])):
                            if rev[ele] == 'Q' and Q >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'W' and W >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'E' and E >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'R' and R >= eachChar:
                                count = len(rev[ele])
                    else:
                        E += 1
                elif string[j] == 'R':
                    if R >= eachChar:
                        rev = string[j::]
                        rev = rev[:: -1]
                        for ele in range(len(rev[len(string) - j + 1])):
                            if rev[ele] == 'Q' and Q >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'W' and W >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'E' and E >= eachChar:
                                count = len(rev[ele])
                            elif rev[ele] == 'R' and R >= eachChar:
                                count = len(rev[ele])
                    else:
                        R += 1
                result = min(result, count)
    return result


print(Solution('QWER'))  # 0
print(Solution('QQWE'))  # 1
print(Solution('QQQW'))  # 2
print(Solution('QQQQ'))  # 3
print(Solution('QWERQQWE'))  # 1
print(Solution("WWQQRRRRQRQQ"))  # 4
print(Solution("WWEQERQWQWWRWWERQWEQ"))  # 4
