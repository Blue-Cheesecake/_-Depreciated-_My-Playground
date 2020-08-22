#include <stdio.h>

void Sort(int *array, int n)
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

int main()
{
    // expect 1 2 2 4 6 6 8 9
    int array[8] = {8, 6, 2, 4, 9, 1, 2, 6};
    Sort(array, 8);
    for (int i = 0; i < 8; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");
    // expect 10 21 28 43 54 76 76 98
    int array2[8] = {10, 54, 76, 28, 98, 43, 76, 21};
    Sort(array2, 8);
    for (int j = 0; j < 8; j++)
    {
        printf("%d ", array2[j]);
    }
    /*6 8 2 4 9 1 2 6
    2 8 6 4 9 1 2 6
    1 8 6 4 9 2 2 6
    1 6 8 4 9 2 2 6
    1 4 6 8 9 2 2 6
    1 2 6 8 9 4 2 6
    1 2 4 8 9 6 2 6
    1 2 2 8 9 6 4 6
    1 2 2 6 8 9 4 6
    1 2 2 4 8 9 6 6
    1 2 2 4 6 9 8 6
    1 2 2 4 6 8 9 6
    1 2 2 4 6 6 9 8
    1 2 2 4 6 6 8 9 */
    return 0;
}