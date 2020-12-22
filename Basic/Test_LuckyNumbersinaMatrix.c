// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

#include <stdio.h>

int main()
{
    int m, n;
    scanf("%d %d", &m, &n);
    int list[m][n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &list[i][j]);
        }
    }

    // find the minimum in each row
    // check if it maximum in column or not
    for (int i = 0; i < m; i++)
    {
        // find min in list[i]
        int min = 0;
        int indexUp = 0;
        int staticCol = 0;
        for (int j = 0; j < n; j++)
        {
            if (j == 0)
            {
                min = list[i][j];
                indexUp = i;
                staticCol = j;
            }
            else
            {
                if (list[i][j] < min)
                {
                    min = list[i][j];
                    indexUp = i;
                    staticCol = j;
                }
            }
        }
        int indexDown = indexUp;
        int True = 1;
        while (indexUp >= 0)
        {
            if (list[indexUp][staticCol] > min)
            {
                True = 0;
                break;
            }
            indexUp -= 1;
        }
        while (indexDown < m)
        {
            if (list[indexDown][staticCol] > min)
            {
                True = 0;
                break;
            }
            indexDown += 1;
        }
        if (True == 1)
        {
            printf("%d ", list[i][staticCol]);
        }
    }
    return 0;
}