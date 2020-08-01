

def ChangedDirection(vert, horz, limit):
    # vert down and up    horz right and left
    Vertical = []
    Horizontal = []
    if vert + 1 <= limit:
        Vertical[0] = vert + 1
    else:
        Vertical[0] = None
    if vert - 1 >= 0:
        Vertical[1] = vert - 1
    else:
        Vertical[1] = None
    if horz + 1 <= limit:
        Horizontal[0] = horz + 1
    else:
        Horizontal[0] = None
    if horz - 1 >= 0:
        Horizontal[1] = horz - 1
    else:
        Horizontal[1] = None
    return Vertical, Horizontal


# def Possibility():


def Solution(board=list, word=str):
    # find index of ini
    ini = word[0]
    result = True
    for i in range(len(board)):
        if ini in board[i]:
            # the next index of  next value
            Vertical, Horizontal = ChangedDirection(
                i, board[i].index(ini), len(board))
            # the dicrection can't return
            # if previous go right, the current can't go left
            # j might appear multiple of dicrection
            # find all possibility of the j
            # if j appear i, n-loop = i
            # if j does not exist result = False (if find all possibility)
            # for j in word[1:]:

    return -1


print(Solution([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "ABCCED"))
