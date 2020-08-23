// https://leetcode.com/problems/remove-element/

#include <stdio.h>

// method for remove element by index
void pop(int index, int *nums, int numSize)
{
    for (int i = 0; i < numSize; i++)
    {
        if (i == index)
        {
            for (int j = i; j < numSize + 1; j++)
            {
                nums[j] = nums[j + 1];
            }
        }
    }
}

int Solution(int *nums, int numSize, int val)
{
    int i = 0;
    while (i < numSize)
    {
        if (nums[i] == val)
        {
            pop(i, nums, numSize);
            numSize--;
        }
        else
        {
            i++;
        }
    }
    return numSize;
}

int main()
{
    // if we just print out there is no problems because it can be printed in actualsize after remove element but I need to modify array correctly
    int t1[4] = {3, 2, 2, 3};
    int val1 = 3;
    int ActualSize = Solution(t1, 4, val1);
    // actuacl t1 array after called fucntion = t[4] [0]=2 [1]=2 [2]=6422352 [3]=4201323
    // but I need only t[2] [0]=2 [1]=2
    for (int i = 0; i < ActualSize; i++)
    {
        printf("%d ", t1[i]);
    }
    printf("\n");

    int t2[8] = {0, 1, 2, 2, 3, 0, 4, 2};
    int val2 = 2;
    int ActualSize2 = Solution(t2, 8, val2);
    // actuacl t1 array after called fucntion = t[4] [0]=0 [1]=1 [2]=3 [3]=0 [4]=4 [5]=2 [6]=2 [7]=2
    // but I need only t[5] [0]=0 [1]=1 [2]=3 [3]=0 [4]=4
    for (int j = 0; j < ActualSize2; j++)
    {
        printf("%d ", t2[j]);
    }
    printf("\n");
    return 0;
}