#include <stdio.h>

// printout
/* *****
    ****
     ***
      **
       *   
    
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
    
    *ooo
    **oo
    ***o
    ****

    0 1 0 1 0
    1 0 1 0 1
    0 1 0 1 0
    1 0 1 0 1
    .
    .
    N line
*/

int main()
{
    int givenN = 5;
    int space = 0;
    for (int i = 0; i < 5; i++)
    {
        int count = 0;
        for (int j = 0; j < space; j++)
        {
            printf(" ");
        }
        while (count < givenN)
        {
            printf("*");
            count += 1;
        }
        givenN -= 1;
        space += 1;
        printf("\n");
    }

    int half = 5;
    int expect = 1;
    int count = 0;
    while (count < half)
    {
        for (int i = 0; i < expect; i++)
        {
            printf("*");
        }
        expect += 1;
        count += 1;
        printf("\n");
    }
    while (count > 0)
    {
        for (int j = 0; j < count - 1; j++)
        {
            printf("*");
        }
        count -= 1;
        printf("\n");
    }

    int expecte = 1;
    int all = 4;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < expecte; j++)
        {
            printf("*");
        }
        for (int k = 0; k < all - expecte; k++)
        {
            printf("o");
        }
        printf("\n");
        expecte += 1;
    }

    int start = 0;
    // n line
    int totalLine = 4;
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            if (start == 0)
            {
                printf("0 ");
                start += 1;
            }
            else
            {
                printf("1 ");
                start -= 1;
            }
        }
        printf("\n");
        if (i % 2 == 0)
        {
            start = 1;
        }
        else
        {
            start = 0;
        }
    }

    return 0;
}