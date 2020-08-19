#include <stdio.h>

int main()
{
    int a = 0;
    while (a != 10)
    {
        printf("Current a : %d\n", a);
        if (a % 2 == 0)
        {
            printf("a is now even\n");
        }
        else
        {
            printf("a is now odd\n");
        }
        a += 1;
    }

    for (int i = 0; i < 10; i++)
    {
        printf("Current i : %d\n", i);
    }

    do
    {
        a += 2;
        printf("Current a : %d\n", a);
    } while (a < 20);

    return 0;
}