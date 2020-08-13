# credit: https://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list


def list_duplicates_of(seq, item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs


A = [1, 2, 3, 2, 4, 6, 4, 2]
print(list_duplicates_of(A, 2))

# test TLE 
# pass in 10^6
B = [1] * 10**6
print(len(list_duplicates_of(B, 1)))
