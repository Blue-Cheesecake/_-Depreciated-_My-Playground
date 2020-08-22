#include <stdio.h>

// loop executions below are equal each others.
int main()
{
    /* local variable definition */
    /* do loop execution */
    // do, while and for is going to loop if condition is True, if in loop cause condition is False, it will  be stopped immidietly
    int a = 10;
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

    } while (a < 20); // condition <---
    // code in loop will do untill a >= 20
    do
    {
        if (a != 15)
        {
            printf("value of a: %d\n", a);
        }
        a += 1;
    } while (a < 20);

    int b = 10;
    do
    {
        if (b != 15)
        {
            printf("value of b: %d\n", b);
        }
        b += 1;
    } while (b < 20);
    // initilize with i = 10 and do code untill i < 20
    for (int i = 10; i < 20; i++)
    {
        if (i != 15)
        {
            printf("value of i: %d\n", i);
        }
    }

    return 0;
}