// https://leetcode.com/explore/featured/card/fun-with-arrays/523/conclusion/3231/

#include <stdio.h>

int removeDuplicate(int *list, int n)
{
    int newSize = 0;
    int hold[n];
    for (int set = 0; set < n; set++)
    {
        hold[n] = 'N';
    }
    for (int i = 0; i < n; i++)
    {
        int add = 1;
        for (int j = 0; j < newSize; j++)
        {
            if (hold[j] == list[i])
            {
                add = 0;
            }
        }
        if (add == 1)
        {
            hold[newSize] = list[i];
            newSize += 1;
        }
    }
    for (int nu = 0; nu < newSize + 1; nu++)
    {
        list[nu] = hold[nu];
    }

    return newSize;
}

void Sort(int *array, int n)
{
    int tmp;
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (array[j] < array[i])
            {
                tmp = array[i];
                array[i] = array[j];
                array[j] = tmp;
            }
        }
    }
}

int Solution(int *nums, int nSize)
{
    // remove duplicate
    nSize = removeDuplicate(nums, nSize);
    // sort
    Sort(nums, nSize);
    if (nSize >= 3)
    {
        return nums[nSize - 3];
    }
    else if (nSize == 2)
    {
        return nums[1];
    }
    else
    {
        return nums[0];
    }
}

int main()
{
    int t1[] = {3, 2, 1};
    printf("%d\n", Solution(t1, 3));
    // 1
    int t2[] = {2, 2, 3, 1};
    printf("%d\n", Solution(t2, 4));

    // 1
    int t3[] = {3, 2, 1, 5435, 6436, 6435, 3, 35, 6, 5, 4, 8, 456, 345, 34656, 445};
    printf("%d\n", Solution(t3, 16));
    // 6435

    return 0;
}