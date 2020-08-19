#include <stdio.h>
// Plating Rock, Paper, or Scisscor
int main()
{
    char inputA = 'P';
    char inputB = 'S';
    if (inputA == 'P')
    {
        if (inputB == 'S')
        {
            printf("Fail");
        }
        else if (inputB == 'R')
        {
            printf("Won");
        }
        else if (inputB == 'P')
        {
            printf("Draw");
        }
        else
        {
            printf("InputB does not exist in option");
        }

    }
    else if (inputA == 'S')
    {
        if (inputB == 'S')
        {
            printf("Draw");
        }
        else if (inputB == 'R')
        {
            printf("Fail");
        }
        else if (inputB == 'P')
        {
            printf("Won");
        }
        else
        {
            printf("InputB does not exist in option");
        }
    }
    else if (inputA == 'R')
    {
        if (inputB == 'S')
        {
            printf("Won");
        }
        else if (inputB == 'R')
        {
            printf("Draw");
        }
        else if (inputB == 'P')
        {
            printf("Fail");
        }
        else
        {
            printf("InputB does not exist in option");
        }
    }
    else
    {
        printf("InputA does not exist in option");
    }
    return 0;
}