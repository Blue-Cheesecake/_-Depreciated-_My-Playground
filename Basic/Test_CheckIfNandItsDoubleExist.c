// https://leetcode.com/problems/check-if-n-and-its-double-exist/

#include <stdio.h>

int Solution(int *arr, int Size)
{
    // check if arr[i] * 2 in a[i+1:] or arr[i] / 2 in arr[i+1:]
    for (int i = 0; i < Size; i++)
    {
        for (int j = i + 1; j < Size; j++)
        {
            if (arr[j] == arr[i] * 2 || arr[j] == arr[i] / 2)
            {
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    int t1[4] = {10, 2, 5, 3};
    printf("%d\n", Solution(t1, 4));
    // for more test case, please look at my Python Solution
    return 0;
}