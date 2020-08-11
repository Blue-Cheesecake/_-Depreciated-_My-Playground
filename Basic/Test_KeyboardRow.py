# https://leetcode.com/problems/keyboard-row/


def Solution(words):
    RowTags = {'a': 2, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 2, 'g': 2, 'h': 2, 'i': 1, 'j': 2, 'k': 2, 'l': 2,
               'm': 3, 'n': 3, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 2, 't': 1, 'u': 1, 'v': 3, 'w': 1, 'x': 3, 'y': 1, 'z': 3}
    result = []
    for i in words:
        base = RowTags.get(i[0].lower())
        add = True
        for j in i.lower():
            if RowTags.get(j) != base:
                add = False
                break
        if add:
            result.append(i)
    return result


print(Solution(["Hello", "Alaska", "Dad", "Peace"]))
