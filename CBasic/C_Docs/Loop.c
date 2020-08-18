#include <stdio.h>

// loop executions below are equal each others.
int main()
{
    /* local variable definition */
    int a = 10;
    /* do loop execution */
    do
    {
        if (a == 15)
        {
            /* skip the iteration */
            a += 1;
        }
        else
        {
            printf("value of a: %d\n", a);
            a += 1;
        }

    } while (a < 20);
    // do
    // {
    //     if (a != 15)
    //     {
    //         printf("value of a: %d\n", a);
    //     }
    //     a += 1;
    // } while (a < 20);

    int b = 10;
    do
    {
        if (b != 15)
        {
            printf("value of b: %d\n", b);
        }
        b += 1;
    } while (b < 20);
    for (int i = 10; i < 20; i++)
    {
        if (i != 15)
        {
            printf("value of i: %d\n", i);
        }
    }

    return 0;
}