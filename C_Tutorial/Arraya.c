#include <stdio.h>

int main()
{
    int array[5] = {1, 2, 3, 4, 5};
    int hold[5];
    for (int i = 0; i < 5; i++)
    {
        hold[i] = array[i];
    }
    for (int k = 0; k < 5; k++)
    {
        if (k == 4)
        {
            printf("%d\n", array[k]);
        }
        else
        {
            printf("%d, ", array[k]);
        }
    }
    for (int j = 0; j < 5; j++)
    {
        if (j == 4)
        {
            printf("%d\n", hold[j]);
        }
        else
        {
            printf("%d, ", hold[j]);
        }
    }
}