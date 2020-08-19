#include <stdio.h>

// not worked
int append(int *array, int length, int add)
{
    int len = length + 1;
    int hold[] = {};
    int *pointer;
    pointer = &array[0];
    for (int i = 0; i < len; i++)
    {
        hold[i] = *pointer;
        pointer++;
    }
    hold[len] = add;
    return hold;
}

int main()
{
    // int array[4] = {1, 2, 3, 4};
    // int hold[5] = {};
    // for (int i = 0; i < 4; i++)
    // {
    //     hold[i] = array[i];
    // }
    // for (int j = 0; j < 4; j++)
    // {
    //     printf("%d ", array[j]);
    // }
    // hold[4] = 5;
    // printf("\n");
    // for (int k = 0; k < 5; k++)
    // {
    //     printf("%d ", hold[k]);
    // }

    int list[] = {1, 2, 3, 4};
    int *AfterAdd;
    AfterAdd = append(list, 4, 5);
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", AfterAdd[i]);
    }

    return 0;
}