def Solution(word=str):
    result = True
    if word != word.capitalize():
        if word != word.lower():
            if word != word.upper():
                result = False
    return result


print(Solution('USA'))  # True
print(Solution('leetcode'))  # True
print(Solution('Google'))  # True
print(Solution('LeetCode'))  # False
print(Solution('LeetcodE'))  # False
