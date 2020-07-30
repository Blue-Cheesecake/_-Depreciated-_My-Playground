# compare length of words
# printf the minimum length in increasing order
# If two words have the same length, arrange them in their original order.


def Solution(text=str):
    freq = {}
    for i in text.split():
        if i not in freq:
            freq[i.lower()] = len(i)
    LengthOrder = sorted(freq.items(), key=lambda kv: kv[1])
    result = ''
    first = True
    # need to compare them in original order if they have same length
    for j in LengthOrder:
        if first:
            result += j[0].capitalize() + ' '
            first = False
        else:
            result += j[0] + ' '
    return result


print(Solution(text="Leetcode is cool"))
print(Solution(text="Keep calm and code on"))
print(Solution(text="To be or not to be"))
