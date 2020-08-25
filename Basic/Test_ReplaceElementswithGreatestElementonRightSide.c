// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

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

void Solution(int *arr, int aSize)
{
    int maxSofar = arr[aSize - 1];
    arr[aSize - 1] = -1;
    for (int i = aSize - 2; i >= 0; i--)
    {
        int temp = arr[i];
        arr[i] = maxSofar;
        maxSofar = max(temp, maxSofar);
    }
}

int main()
{
    int t1[6] = {17, 18, 5, 4, 6, 1};
    Solution(t1, 6);
    for (int i = 0; i < 6; i++)
    {
        printf("%d ", t1[i]);
    }
    return 0;
}