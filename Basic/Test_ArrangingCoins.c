// https://leetcode.com/problems/arranging-coins/

#include <stdio.h>
#define INT_MAX 2147483647

int Solution(int n)
{
    int count;
    if (n <= INT_MAX)
    {
        count = 0;
        int left = n;
        for (int i = 1; i < n + 1; i++)
        {
            left -= i;
            if (left >= 0)
            {
                count += 1;
            }
            else
            {
                break;
            }
        }
    }
    return count;
}

int main()
{
    int t1 = 5;  // 2
    int t2 = 10; // 4
    printf("%d %d", Solution(t1), Solution(t2));
    return 0;
}