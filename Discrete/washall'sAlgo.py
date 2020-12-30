def wli(mat: list):
    n = len(mat)
    print("W0")
    for i in mat:
        print(i)
    for i in range(n):
        # find index 1 at col and row
        pos_row = []
        row = 0
        for j in range(n):
            if mat[i][j] == 1:
                pos_row.append(j)
                row += 1

        pos_col = []
        col = 0
        index_col = i + 0
        for index_row in range(n):
            if mat[index_row][index_col] == 1:
                pos_col.append(index_row)
                col += 1

        for pc in pos_col:
            for pr in pos_row:
                mat[pc][pr] = 1

        # print(f"row:{row} col:{col} at {i}")
        # print(pos_col, pos_row)
        print(f"W{i + 1}")
        for j in range(n):
            print(mat[j])
        # print("\n")


def warshall(a):
    assert (len(row) == len(a) for row in a)
    n = len(a)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
    return a


if __name__ == "__main__":
    # print(warshall([[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [
    # 0, 1, 1, 0, 1], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0]]))
    # wli([[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [
    #     0, 1, 1, 0, 1], [0, 1, 0, 0, 0], [1, 0, 0, 1, 0]])
    # wli([[0, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]])

    n = input("n : ")
    n = int(n)
    t = []
    for i in range(n):
        row = []
        for j in range(n):
            store = input(f"index {i+1} {j+1} >> ")
            row.append(int(store))
        t.append(row)
    # print(t)
    wli(t)

    pass
