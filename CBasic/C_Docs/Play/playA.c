#include <stdio.h>

int main()
{
    char p[] = "cash";
    if (p == "cash")
    {
        printf("True");
    }
    else
    {
        // False
        printf("False\n");
    }
    int Boolean = 1;
    for (int i = 0; i < 4; i++)
    {
        if (p[i] != 'c' && p[i] != 'a' && p[i] != 's' && p[i] != 'h')
        {
            Boolean = 0;
        }
    }
    switch (Boolean)
    {
    case 1:
        printf("condition if True");
        break;

    case 0:
        printf("condition if False");
    default:
        break;
    }

    return 0;
}