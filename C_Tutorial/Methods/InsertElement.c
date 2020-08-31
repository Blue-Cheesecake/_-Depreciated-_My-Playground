#include <stdio.h>
#define MAX_SIZE 100

// return new size
int insert(int *list, int size, int index, int elem)
{
    // check if index is Valid
    if (index > size || index < 0)
    {
        // raise error
    }
    // shifting from i (index that insert)
    for (int i = size; i >= index; i--)
    {
        list[i] = list[i - 1];
    }
    list[index] = elem;
    return size + 1;
}

int main()
{
    int arr[MAX_SIZE] = {8, 7, 4, 3, 6};
    int n = 5;
    n = insert(arr, n, 2, 999);
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}