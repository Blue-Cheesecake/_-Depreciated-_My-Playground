// https://leetcode.com/problems/squares-of-a-sorted-array/

#include <stdio.h>

void Sort(int array[], int n)
{
    int tmp;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (array[j] < array[i])
            {
                tmp = array[i];
                array[i] = array[j];
                array[j] = tmp;
            }
        }
    }
}

void Solution(int A[], int n)
{
    for (int i = 0; i < n; i++)
    {
        A[i] = A[i] * A[i];
    }
    Sort(A, n);
}

int main()
{
    int list[5] = {-4, -1, 0, 3, 10};
    // 0 1 9 16 100
    Solution(list, 5);
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", list[i]);
    }

    return 0;
}