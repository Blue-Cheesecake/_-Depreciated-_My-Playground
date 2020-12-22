// https://leetcode.com/problems/merge-sorted-array/
// just merge it and sort them

#include <stdio.h>

// sort method
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

void Solution(int *nums1, int m, int *nums2, int n)
{
    int index = 0;
    for (int i = m; i < m + n; i++)
    {
        nums1[i] = nums2[index];
        index++;
    }
    // sort
    Sort(nums1, m + n);
}

int main()
{
    int at1[6] = {1, 2, 3, 0, 0, 0};
    int m = 3;
    int at2[3] = {2, 5, 6};
    int n = 3;
    Solution(at1, m, at2, n);
    for (int i = 0; i < 6; i++)
    {
        printf("%d ", at1[i]);
    }

    return 0;
}