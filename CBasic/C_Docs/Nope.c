#include <stdio.h>
#include <stdlib.h>

void append(int array[], int iter, int len)
{
    array[len] = iter;
}

int main()
{
    int arr[] ={ 6, 5, 4, 3, 2, 88 };
    arr[7] = 6;
    // append(arr, 10, 5);
    for (int i = 0; i < 7; i++)
    {
        printf("%d ", arr[i]);
    }
    return 0;
}