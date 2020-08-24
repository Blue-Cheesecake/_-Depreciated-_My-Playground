#include <stdio.h>

// remove by index
// rotate from i + 1 (i = index that want to be removed) to i
void pop(int index, int *nums, int numSize)
{
    for (int i = 0; i < numSize; i++)
    {
        if (i == index)
        {
            for (int j = i; j < numSize + 1; j++)
            {
                nums[j] = nums[j + 1];
            }
        }
    }
}

int main()
{
    int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    pop(2, array, 10);
    for (int i = 0; i < 9; i++)
    {
        printf("%d ", array[i]);
    }
    return 0;
}