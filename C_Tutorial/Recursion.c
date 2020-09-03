#include <stdio.h>

// Recursion means the function that call its function itself.
int BinarySearch(int array[], int low, int high, int find)
{
    int mid = (high + low) / 2;
    if (find == array[mid])
    {
        return mid;
    }
    else
    {
        if (find < array[mid])
        {
            high = mid;
            return BinarySearch(array, low, high, find);
        }
        else if (find > array[mid])
        {
            low = mid;
            return BinarySearch(array, low, high, find);
        }
    }
}
// sequence 1 1 2 3 5 8 13 21 ....
int fibonacci(int n)
{
    if (n <= 2)
    {
        return 1;
    }
    else
    {
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

int main()
{
    int arr[6] = {1, 2, 3, 4, 5, 6};
    int low = 0;
    int high = 6;
    printf("%d\n", BinarySearch(arr, low, high, 5));
    printf("%d ", fibonacci(5));
    return 0;
}