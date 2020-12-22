# https://programming.in.th/task/rev2_problem.php?pid=1154


def right_in_left_out(string, num):
    k = 0
    while num + k <= len(string):
        if k == 0:
            yield string[0:num]
            k += 1
        else:
            yield string[k:num + k]
            k += 1


def LongestRepeated(M, S):
    storage = []
    R = 1
    while R <= len(S):
        base = S[0:R]
        occurence = 0
        substring = [i for i in right_in_left_out(S, len(base))]
        for j in substring:
            if occurence < M:
                if base == j:
                    occurence += 1
            else:
                storage.append(base)
                break
        R += 1
    largest = 0
    for k in storage:
        if len(k) >= largest:
            largest = len(k)
    return largest


print(LongestRepeated(2, 'oybjfoybjl'))
print(LongestRepeated(5, 'ohpjooooyc'))
