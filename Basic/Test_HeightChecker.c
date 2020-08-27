// https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3228/

#include <stdio.h>

void sort(int *arr, int size)
{
    int temp;
    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            if (arr[j] < arr[i])
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int Solution(int *height, int hSize)
{
    int count = 0;
    // create sorted array
    int sortedH[hSize];
    for (int i = 0; i < hSize; i++)
    {
        sortedH[i] = height[i];
    }
    // compared with sorted array
    sort(sortedH, hSize);
    int index = 0;
    while (index < hSize)
    {
        if (height[index] != sortedH[index])
        {
            count += 1;
        }
        index += 1;
    }

    return count;
}
int main()
{
    int t1[6] = {1, 1, 4, 2, 1, 3};
    printf("%d ", Solution(t1, 6));
    int t2[5] = {5, 1, 2, 3, 4};
    printf("%d ", Solution(t2, 5));
    return 0;
}