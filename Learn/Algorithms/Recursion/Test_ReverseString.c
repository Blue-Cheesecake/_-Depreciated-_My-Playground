//  https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1440/

// Do not return anything, modify s in-place instead.

// Approach 1
// Time  complexity : O(N)
// Space complexity : O(N)

#include <stdio.h>

void recursinInPlace(int *s, int left, int right)
{
    //  implement recursive function helper which receives two pointers, left and right, as arguments.
    //  Base case: if left >= right, do nothing.
    //  Otherwise, swap s[left] and s[right] and call helper(left + 1, right - 1).
    // To solve the problem, passing the head and tail indexes as arguments: return helper(0, len(s) - 1).
    if (left >= right)
    {
        // pass
    }
    else
    {
        // swap
        int temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        recursinInPlace(s, left + 1, right - 1);
    }
}

int twoPointersIteration(int *s, int sSize)
{
    // initial left = the first index, right = the last index
    int left = 0;
    int right = sSize - 1;
    while (left < right)
    {
        // swap
        int temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        // move to the next index
        left += 1;
        right -= 1;
    }
}

int main()
{
    int t1[6] = {1, 2, 3, 4, 5, 6};
    int i;
    for (i = 0; i < 6; i++)
    {
        printf("%d ", t1[i]);
    }
    printf("\n");
    // remove // before one function to see result
    // recursinInPlace(t1, 0, 6 - 1);
    // twoPointersIteration(t1, 6);
    for (i = 0; i < 6; i++)
    {
        printf("%d ", t1[i]);
    }

    return 0;
}