inp = ['HEAD', 'HEAP', 'LEAP', 'TEAR', 'REAR', 'BAER',
       'BAET', 'BEEP', 'JEEP', 'JOIP', 'JEIP', 'AEIO']

contin = True
while contin:
    for i in range(len(inp)):
        try:
            count = 0
            for j, k in zip(inp[i], inp[i+1]):
                if j != k:
                    count += 1
                if count > 2:
                    print(inp[i])
                    contin = False
                    break
            count = 0
        except IndexError:
            pass
        if not contin:
            break
