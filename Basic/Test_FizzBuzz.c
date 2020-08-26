#include <stdio.h>

void Solution(int n)
{
    for (int i = 1; i < n + 1; i++)
    {
        if (i % 3 == 0 && i % 5 == 0)
        {
            printf("FizzFuzz ");
        }
        else if (i % 3 == 0)
        {
            printf("Fizz ");
        }
        else if (i % 5 == 0)
        {
            printf("Buzz ");
        }
        else
        {
            printf("%d ", i);
        }
    }
}

int main()
{
    int t1 = 15;
    Solution(t1);
    return 0;
}