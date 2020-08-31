#include <stdio.h>
#define MAX_SIZE 10000

void append(int *arr, int size, int element)
{
    arr[size] = element;
}

int main()
{
    // array declaration must insert MaxSize
    int array[MAX_SIZE] = {1, 2, 3, 4, 5, 6};
    int size, x;
    size = 6;
    x = 999;
    append(array, size, x);
    for (int i = 0; i < size + 1; i++)
    {
        printf("%d ", array[i]);
    }
    return 0;
}