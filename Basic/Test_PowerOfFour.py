# https://leetcode.com/problems/power-of-four/
# solve with no loop or recursion

def Solution(num=int):
    if num < 0:
        return False
    Bivalue = bin(num)
    if Bivalue[::-1].find('1') % 2 == 0 and Bivalue.count('1') == 1:
        return True
    return False


print(Solution(16))
print(Solution(32))
print(Solution(136))

# credit = https://leetcode.com/problems/power-of-four/discuss/772426/Python-no-looprecursion-without-logs-in-O(logn)-with-explanation