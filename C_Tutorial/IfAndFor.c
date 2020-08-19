#include <stdio.h>

int main()
{
    // find only prime factor
    int suspect = 126;
    for (int i = 2; i < suspect + 1; i++)
    {
        if (suspect != 1)
        {
            if (suspect % i == 0)
            {
                while (suspect % i == 0)
                {
                    printf("%d ", i);
                    suspect = suspect / i;
                }
            }
        }
    }

    return 0;
}