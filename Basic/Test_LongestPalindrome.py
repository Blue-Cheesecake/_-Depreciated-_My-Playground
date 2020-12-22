# https://leetcode.com/problems/longest-palindrome/

from collections import Counter


def Solution(s=str):
    reverse = s[::-1]
    if reverse != s:
        Freq = Counter(s)
        count = 0
        PlusOnlyOne = None
        for i in Freq.values():
            if i % 2 == 0:
                count += i
            else:
                if i == 1:
                    PlusOnlyOne = True
                else:
                    count += (i - 1)
                    PlusOnlyOne = True
        if PlusOnlyOne:
            return count + 1
        return count
    else:
        return len(s)


print(Solution(s="abccccdd"))
print(Solution(s="abccccddqwdqwdffffwefwjelfwkjffjfjfjffjfjjjjjjwfewfwef"))
print(Solution(s="cccwefwefwefwefwef"))
print(Solution(s="ccc"))
