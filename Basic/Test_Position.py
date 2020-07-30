A = [1, 1, 4, 2, 1, 3]  # 3
B = [5, 1, 2, 3, 4]  # 5
C = [1, 2, 3, 4, 5]  # 0
G = [2, 1, 2, 1, 1, 2, 2, 1]  # 6
List = A


def b(heights):
    original = list(enumerate(heights))
    after = sorted(heights)
    after = list(enumerate(after))
    count = 0
    for i, j in zip(original, after):
        if i != j:
            count += 1
    return count


print(b(A))
print(b(B))
print(b(C))
print(b(G))
