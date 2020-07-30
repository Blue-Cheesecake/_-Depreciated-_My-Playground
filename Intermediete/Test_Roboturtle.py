def rotated(lst):
    last = lst[0]
    arry = lst
    for i in range(len(lst)):
        try:
            arry[i] = lst[i+1]
        except IndexError:
            arry[len(lst) - 1] = last
    return arry


def rotate_till(lst, indx_direct):
    front = lst[indx_direct]
    while lst[0] != front:
        lst = rotated(lst)
    return lst


command = (('LT', 2), ('RT', 4), ('FD', 3))
coordinate = [0, 0]
coordinate_direct = ['E', 'N', 'W', 'S']
coordinate_plane = ['x', 'y']

for i in command:
    if i[0] == 'LT':
        coordinate_direct = rotate_till(coordinate_direct, 1)
    elif i[0] == 'RT':
        coordinate_direct = rotate_till(coordinate_direct, 3)
    elif i[0] == 'BW':
        coordinate_direct = rotate_till(coordinate_direct, 2)
    if coordinate_direct[0] == 'N':
        coordinate[1] += i[1]
    elif coordinate_direct[0] == 'S':
        coordinate[1] -= i[1]
    elif coordinate_direct[0] == 'E':
        coordinate[0] += i[1]
    elif coordinate_direct[0] == 'W':
        coordinate[0] -= i[1]

if coordinate[0] >= 50000 or coordinate[0] <= -50000 or coordinate[1] >= 50000 or coordinate[1] <= -50000:
    print('DEAD')
else:
    print(coordinate, coordinate_direct[0])
