// https://leetcode.com/problems/the-kth-factor-of-n/

#include <stdio.h>

int Solution(int num, int k)
{
    int fact = 0;
    for (int i = 1; i < num + 1; i++)
    {
        if (num % i == 0)
        {
            fact++;
        }
        if (fact == k)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    int t1 = Solution(12, 3);
    printf("Solution(12,3) = %d\n", t1); // 3
    int t2 = Solution(1000, 16);
    printf("Solution(1000, 16) = %d\n", t2); // 1000
    int t3 = Solution(4, 4);
    printf("Solution(4, 4) = %d\n", t3); // -1
    int t4 = Solution(7, 2);
    printf("Solution(7, 2) = %d\n", t4); // 7
    return 0;
}