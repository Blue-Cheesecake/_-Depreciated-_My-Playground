# https://programming.in.th/task/rev2_problem.php?pid=0035


def powerset(sets):
    result = [[]]
    for i in sets:
        arry = [subset + [i] for subset in result]
        result.extend(arry)
    for j in result:
        if len(j) == 3:
            yield j


def area(p1, p2, p3):
    return (abs(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[1]*p2[0] - p2[1]*p3[0] - p3[1]*p1[0])) / 2


test = [[1, 2], [2, 1], [0, 0], [3, 4], [-1, -2]]
largest_area = 0
position = None
for k in powerset(test):
    cal_area = area(k[0], k[1], k[2])
    if cal_area >= largest_area:
        largest_area = cal_area
        position = k
print(largest_area, position)
