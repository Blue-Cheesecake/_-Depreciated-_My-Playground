// https://leetcode.com/problems/check-if-it-is-a-straight-line/

#include <stdio.h>

int Solution(int coordinates[][2], int size)
{
    // check if x or y are equals to each others
    // if it's all True : return False
    int XAxis = 1;
    int YAxis = 1;
    for (int i = 0; i < size - 1; i++)
    {
        // check X
        if (coordinates[i][0] != coordinates[i + 1][0])
        {
            XAxis = 0;
        }
        // Check Y
        if (coordinates[i][1] != coordinates[i + 1][1])
        {
            YAxis = 0;
        }
    }
    if (XAxis == 1)
    {
        return 1;
    }
    else if (YAxis == 1)
    {
        return 1;
    }
    else
    {
        int DoOneTime = 0;
        float slope;
        for (int j = 0; j < size - 1; j++)
        {
            // except zero division
            if (coordinates[j][0] - coordinates[j + 1][0] == 0)
            {
                return 0;
            }
            else
            {
                // just compute the slope
                if (DoOneTime == 0)
                {
                    slope = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0]);
                    DoOneTime += 1;
                }
                else
                {
                    // if result is not equals to slope: return False
                    if ((coordinates[j][1] - coordinates[j + 1][1]) / (coordinates[j][0] - coordinates[j + 1][0]) != slope)
                    {
                        return 0;
                    }
                }
            }
        }
        return 1;
    }
}

int main()
{
    int t1[6][2] = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}};
    int result1 = Solution(t1, 6);
    // 1
    printf("%d\n", result1);
    int t2[6][2] = {{1, 1}, {2, 2}, {3, 4}, {4, 5}, {5, 6}, {7, 7}};
    int result2 = Solution(t2, 6);
    // 0
    printf("%d\n", result2);
    return 0;
}