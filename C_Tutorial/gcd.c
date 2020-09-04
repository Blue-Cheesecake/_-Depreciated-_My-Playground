#include <stdio.h>

int main()
{
    int a = 18;
    int b = 84;
    int maxi = 0;
    for (int i = 1; i < a + 1; i++)
    {
        if (a % i == 0)
        {
            if (b % i == 0)
            {
                maxi = i;
            }
        }
    }
    printf("%d", maxi);
    return 0;
}