// https://leetcode.com/problems/array-nesting/

#include <stdio.h>

int main()
{
    // int n;
    // scanf("%d", &n);
    // int list[n];
    // for (int i = 0; i < n; i++)
    // {
    //     scanf("%d", &list[n]);
    // }
    // int n = 7;
    // int list[7] = {5, 4, 0, 3, 1, 6, 2};
    // int numsSize = 12;
    // int nums[12] = {10, 5, 4, 11, 0, 3, 1, 6, 2, 7, 8, 9};
    int numsSize = 3;
    int nums[3] = {0, 1, 2};
    int max = 0;
    for (int i = 0; i < numsSize; i++)
    {
        int sizeS = 0;
        int S[numsSize];
        int index = i;
        int dupOrNotExist = 0;
        // check if index exist in hold or not
        while (dupOrNotExist == 0)
        {
            // loop for duplicate
            // if list[index] not in hold
            // add
            // else  break --> out loop
            for (int j = 0; j < sizeS; j++)
            {
                if (nums[index] == S[j])
                {
                    dupOrNotExist = 1;
                }
            }
            if (dupOrNotExist == 0)
            {
                S[sizeS] = nums[index];
                sizeS += 1;
                index = nums[index];
            }
        }
        // max = max(sizeS,max)
        if (sizeS > max)
        {
            max = sizeS;
        }
    }
    printf("%d", max);
    return 0;
}