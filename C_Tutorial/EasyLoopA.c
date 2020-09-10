#include <stdio.h>

int main()
{
    // input must be odd number
    int n = 17;
    int space = 0;
    int temp = n;
    while (temp != 1)
    {
        temp -= 2;
        space += 1;
    }
    // got space
    while (temp != n)
    {
        // print space
        for (int i = 0; i < space; i++)
        {
            printf(" ");
        }
        // print *
        for (int j = 0; j < temp; j++)
        {
            printf("*");
        }
        printf("\n");
        temp += 2;
        space -= 1;
    }

    return 0;
}