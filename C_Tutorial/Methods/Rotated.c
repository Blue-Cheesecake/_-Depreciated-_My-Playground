#include <stdio.h>

void RoratedLeft(int *array, int size)
{
    int temp = array[0];
    for (int i = 0; i < size - 1; i++)
    {
        array[i] = array[i + 1];
    }
    array[size - 1] = temp;
}
// in the other hand, Rotate to the right is the same concept

void RotatedRight(int *array, int size)
{
    int temp = array[size - 1];
    for (int i = size - 1; i > 0; i--)
    {
        array[i] = array[i - 1];
    }
    array[0] = temp;
}

int main()
{
    // expect 2 3 4 5 1
    int list[5] = {1, 2, 3, 4, 5};
    RoratedLeft(list, 5);
    for (int j = 0; j < 5; j++)
    {
        printf("%d ", list[j]);
    }
    printf("\n");
    // expect 5 1 2 3 4
    int listA[5] = {1, 2, 3, 4, 5};
    RotatedRight(listA, 5);
    for (int k = 0; k < 5; k++)
    {
        printf("%d ", listA[k]);
    }
    return 0;
}