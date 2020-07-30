def operator(dat1, oper, dat2):
    if oper == '+':
        return dat1 + dat2
    elif oper == '*':
        return dat1 * dat2
    else:
        return 'Something went wrong'


print(operator(1000, '*', 100))
