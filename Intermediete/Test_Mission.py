# Exercise from Tumso Competition
# source https://programming.in.th/task/rev2_problem.php?pid=1117
# energy and exp are given


def powerset(lst):
    result = [[]]
    for i in lst:
        j = [subset + [i] for subset in result]
        result.extend(j)
    return result


def point_received(energy, exp):
    return exp - (2 * energy)


def loss(point, loss_t):
    return point - (loss_t ** 2)


enrg_exp = [(6, 10), (6, 20), (8, 10), (8, 20)]
num = len(enrg_exp)
powerset = powerset(enrg_exp)
room = []
for i in powerset:
    n_missions = len(i)
    if n_missions == 0:
        point = 0
        for j in enrg_exp:
            point += point_received(j[0], j[1])
        l = loss(point, num)
        room.append(l)
    else:
        l_tasks = num - n_missions
        point = 0
        for k in i:
            point += point_received(k[0], k[1])
        l = loss(point, l_tasks)
        room.append(l)

most_val = 0
for x in room:
    if x > most_val:
        most_val = x

print(most_val)

# solved by Sinut Wattanarporn
