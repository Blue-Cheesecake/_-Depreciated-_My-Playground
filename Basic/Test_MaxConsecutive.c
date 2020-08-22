// # https://leetcode.com/problems/max-consecutive-ones/

#include <stdio.h>

int max(int num1, int num2)
{
    int result;
    if (num1 > num2)
    {
        result = num1;
    }
    else
    {
        result = num2;
    }
    return result;
}

int Solution(int nums[], int size)
{
    int Maximum = 0;
    int i = 0;
    while (i < size)
    {
        int plus = 0;
        int count = 0;
        if (nums[i] == 1)
        {
            count += 1;
            for (int j = i + 1; j < size; j++)
            {
                if (nums[j] == 1)
                {
                    plus += 1;
                    count += 1;
                }
                else
                {
                    break;
                }
            }
        }
        Maximum = max(Maximum, count);
        if (plus > 0)
        {
            i += plus;
        }
        else
        {
            i += 1;
        }
    }
    return Maximum;
}

int main()
{
    int list[6] = {1, 1, 0, 1, 1, 1};
    int listA[10] = {1, 0, 1, 1, 1, 1, 0, 1, 1, 1};
    // 3
    printf("%d\n", Solution(list, 6));
    // 4
    printf("%d\n", Solution(listA, 10));
    return 0;
}