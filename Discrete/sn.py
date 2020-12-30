def S(n, k):
    if k == 1:
        return 1
    if k == n:
        return 1

    return S(n-1, k-1) + k * S(n-1, k)


if __name__ == "__main__":
    n = input("n : ")
    k = input("k : ")
    n = int(n)
    k = int(k)
    print(S(n, k))
    # print("\n")

    s = 0
    i = 1
    while i <= n:
        s += S(n, i)
        i += 1

    print("number of partition:", s)
