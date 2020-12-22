#include <stdio.h>

int main()
{
    int indexN;
    scanf("%d", &indexN);
    if (indexN == 0)
    {
        printf("0");
    }
    else if (indexN == 1)
    {
        printf("1 1");
    }
    else
    {
        int count = 1;
        int initial[41] = {1, 1};
        int hold[41];
        int curSize = 2;
        while (count < indexN)
        {
            curSize += 1;
            for (int i = 0; i < curSize - 1; i++)
            {
                hold[i] = initial[i];
            }
            // add element into initial from hold
            for (int i = 0; i < curSize; i++)
            {
                if (i != curSize - 1 && i != 0)
                {
                    initial[i] = hold[i - 1] + hold[i];
                }
                else
                {
                    initial[i] = 1;
                }
            }
            count += 1;
            if (count == indexN)
            {
                for (int i = 0; i < curSize; i++)
                {
                    printf("%d ", initial[i]);
                }
            }
        }
    }

    return 0;
}