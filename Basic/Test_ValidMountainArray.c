#include <stdio.h>

// Optimal Solution
int Solution(int *A, int ASize)
{
    int i = 0;
    // climb up
    while (i + 1 < ASize && A[i] < A[i + 1])
    {
        i++;
    }
    // check if end or beginning
    if (i == 0 || i == ASize - 1)
    {
        return 0;
    }
    // check down
    while (i + 1 < ASize && A[i] > A[i + 1])
    {
        i++;
    }
    // check index
    if (i == ASize - 1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    int t1[8] = {0, 2, 3, 4, 5, 2, 1, 0};
    printf("%d\n", Solution(t1, 8)); // True
    // for more test case, just check in my Python Solution in the same file name
    return 0;
}