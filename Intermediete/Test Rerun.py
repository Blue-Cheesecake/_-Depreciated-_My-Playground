given = ('o', 'g', 'p')
state = ''
i = 0
day = 0
while True:
    if i <= len(given) - 1:
        if len(state) == 2:
            if state[0] == 'o':
                if day > 1:
                    print(day)
                    break
            day += 1
            state = ''
        else:
            state += given[i]
            i += 1
    else:
        i = 0
