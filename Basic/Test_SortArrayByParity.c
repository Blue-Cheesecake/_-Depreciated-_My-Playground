// https://leetcode.com/problems/sort-array-by-parity/
#include <stdio.h>

// concept --> separete even and odd in another array and merge it
void Solution(int *A, int size)
{
    int even[size];
    int actualEvenSize = 0;
    int odd[size];
    int actualOddSize = 0;
    int merge[size];
    for (int i = 0; i < size; i++)
    {
        if (A[i] % 2 == 0)
        {
            //    add into even list
            even[actualEvenSize] = A[i];
            actualEvenSize++;
        }
        else
        {
            //    add into odd list
            odd[actualOddSize] = A[i];
            actualOddSize++;
        }
    }
    int j;
    for (j = 0; j < actualEvenSize; j++)
    {
        merge[j] = even[j];
    }
    // fix with initialil temp variable for odd start at index 0
    for (int k = j, i = 0; i < actualOddSize; k++, i++)
    {
        merge[k] = odd[i];
    }

    for (int l = 0; l < size; l++)
    {
        A[l] = merge[l];
    }
}

int main()
{
    // order is not matter
    int t1[4] = {3, 1, 2, 4};
    Solution(t1, 4);
    for (int i = 0; i < 4; i++)
    {
        printf("%d ", t1[i]);
    }
    return 0;
}