#include <stdio.h>

// if syntax

int main()
{
    int num = 100;
    if (num % 2 == 0)
    {
        printf("num is even numbers (%d)\n", num);
    }
    else
    {
        printf("nums is odd numbers (%d)\n", num);
    }
    int num2 = 10;
    if (num2 % 2 == 0)
    {
        printf("num is even numbers (%d)\n", num2);
        if (num2 % 4 != 0)
        {
            printf("number cant be divided by 4 (%d)\n", num2);
        }
    }
    else
    {
        printf("nums is odd numbers (%d)\n", num2);
    }
    // switch act like if, it's separated into many case(if var equal to caseN)
    switch (num2)
    {
    case 10:
        printf("num2 value is 10");
        break;

    // if have no case to express:
    // defaut = else:
    default:
        break;
    }
    
    return 0;
}