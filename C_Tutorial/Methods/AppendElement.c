#include <stdio.h>
#define MAX_SIZE 10000

int main()
{
    // no need to turn to function since it can be simplified
    int array[MAX_SIZE] = {1, 2, 3, 4, 5, 6};
    int size, x;
    size = 6;
    x = 999;
    array[size] = x;
    for (int i = 0; i < size + 1; i++)
    {
        printf("%d ", array[i]);
    }

    return 0;
}