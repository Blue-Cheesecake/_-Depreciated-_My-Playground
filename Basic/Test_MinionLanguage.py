# Sorce : Google Interview FooBar

#input: "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
# outout:  Yeah! I can't believe Lance lost his job at the colony!!
# lower case do reverse but Upper case dont


def solution(x):
    reverse = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's',
               'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h',
               't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'
               }
    state = ''
    for i in range(len(x)):
        for j in reverse.items():
            if x[i] == j[0]:
                state += j[1]
                break
        if x[i] not in reverse.keys():
            state += x[i]
    return state


print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
