#include <stdio.h>

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

int main()
{
    int arr[6] ={ 1, 2, 3, 4, 5, 6 };
    int low = 0;
    int high = 6;
    printf("%d", BinarySearch(arr, low, high, 5));
    return 0;
}