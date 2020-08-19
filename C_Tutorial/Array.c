#include <stdio.h>
#include <stdlib.h>

int main()
{
    // type arrayName [arraySize ];
    // we can access more dimension array : arr[i][j][...]
    // types of array must be respected by types of Data (int,float char etc.)
    int numbers[] = {1, 4, 2, 6, 4, 8, 9};
    for (int i = 0; i < 7; i++)
    {
        if (numbers[i] % 2 == 0)
        {
            printf("%d is even number\n", numbers[i]);
        }
        else
        {
            printf("%d is odd number\n", numbers[i]);
        }
    }
    // print entire array
    for (int k = 0; k < 7; k++)
    {
        if (k == 6)
        {
            printf("%d\n", numbers[k]);
        }
        else
        {
            printf("%d, ", numbers[k]);
        }
    }
    // try to change elements (it's work)
    for (int j = 0; j < 7; j++)
    {
        if (numbers[j] % 2 == 0)
        {
            numbers[j] = 0;
        }
        else
        {
            numbers[j] = 1;
        }
    }
    // it's work
    for (int l = 0; l < 7; l++)
    {
        if (l == 6)
        {
            printf("%d\n", numbers[l]);
        }
        else
        {
            printf("%d, ", numbers[l]);
        }
    }
    int temp = numbers[0];
    for (int I = 0; I < 6; I++)
    {
        numbers[I] = numbers[I + 1];
    }
    numbers[6] = temp;
    for (int Y = 0; Y < 7; Y++)
    {
        if (Y == 6)
        {
            printf("%d\n", numbers[Y]);
        }
        else
        {
            printf("%d, ", numbers[Y]);
        }
    }
    return 0;
}