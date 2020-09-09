# https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/

# Do not return anything, modify s in-place instead.

# Approach 1
# Time  complexity : O(N)
# Space complexity : O(N)


def recursinInPlace(s=list):
    # implement recursive function helper which receives two pointers, left and right, as arguments.
    # Base case: if left >= right, do nothing.
    #  Otherwise, swap s[left] and s[right] and call helper(left + 1, right - 1).
    # To solve the problem, call helper function passing the head and tail indexes as arguments: return helper(0, len(s) - 1).
    def helper(left, right):
        if left >= right:
            pass
        else:
            # swap
            s[left], s[right] = s[right], s[left]
            # move to the next index
            helper(left + 1, right - 1)
    # initial left = the first index, right = the last index
    helper(0, len(s) - 1)

# Approach 2
# Time  complexity : O(N)
# Space complexity : O(1)


def twoPointersIteration(s=list):
    # initial left = the first index, right = the last index
    left = 0
    right = len(s) - 1
    while left < right:
        # swap
        s[left], s[right] = s[right], s[left]
        # move to the next index
        left += 1
        right -= 1


t1 = ['h', 'e', 'l', 'l', 'o']
print(t1)
recursinInPlace(t1)
print(t1)

t2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(t2)
twoPointersIteration(t2)
print(t2)
