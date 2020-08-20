#include <stdio.h>

int factorial(int num)
{
    int result = 1;
    for (int i = 1; i < num + 1; i++)
    {
        result *= i;
    }
    return result;
}

int main()
{
    int e = factorial(4);
    printf("%d ", e);
    return 0;
}