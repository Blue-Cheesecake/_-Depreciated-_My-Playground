#include <stdio.h>

int Solution(int *nums, int nSize, int k)
{
    int oneExist = 0;
    int i = 0;
    int j = 0;
    while (i < nSize)
    {
        if (nums[i] == 1)
        {
            oneExist = 1;
            int countZero = 0;
            int countTime = 0;
            if (i == nSize - 1)
            {
                break;
            }
            j = i + 1;
            while (countTime < k)
            {
                if (nums[j] == 0)
                {
                    countZero += 1;
                }
                countTime += 1;
                j += 1;
            }
            if (countZero < k)
            {
                return 0;
            }
            i = j;
        }
        else
        {
            i += 1;
        }
    }
    return 1;
}

int main()
{
    // nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2
    int numsA[] = {1, 0, 0, 0, 1, 0, 0, 1};
    int numsB[] = {1, 0, 0, 1, 0, 1};
    int numsC[] = {1, 1, 1, 1, 1};
    int numsD[] = {0, 1, 0, 1};
    printf("%d ", Solution(numsA, 8, 2));
    // True
    printf("%d ", Solution(numsB, 6, 2));
    // False
    printf("%d ", Solution(numsC, 5, 0));
    // True
    printf("%d ", Solution(numsD, 4, 1));
    // True
    return 0;
}