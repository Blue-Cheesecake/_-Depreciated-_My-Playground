#include <stdio.h>

int tribonacci(int n)
{
    int dynamic[38] = {0};
    for (int i = 0; i < 3; i++)
    {
        if (i != 0)
        {
            dynamic[i] = 1;
        }
    }
    int actualSize = 3;
    for (int i = 0; i < n + 1; i++)
    {
        if (n <= actualSize - 1)
        {
            return dynamic[n];
        }
        dynamic[i + 3] = dynamic[i] + dynamic[i + 1] + dynamic[i + 2];
        actualSize += 1;
    }
}

int main()
{
    printf("%d ", tribonacci(36));
    return 0;
}