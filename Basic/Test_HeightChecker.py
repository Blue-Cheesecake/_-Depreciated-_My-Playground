# https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3228/

def Solution(heights=list):
    # compare to the sort
    compare = sorted(heights)
    count = 0
    for i, j in zip(enumerate(heights), enumerate(compare)):
        if i[1] != j[1]:
            count += 1
    return count


print(Solution(heights=[1, 1, 4, 2, 1, 3]))  # 3
