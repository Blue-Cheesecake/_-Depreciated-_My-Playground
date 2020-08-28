#include <stdio.h>

int main()
{
    // char varName[MaximumSizeOfString]
    char string[20];
    // input string
    scanf(" %s", &string);
    printf("%s\n", string);

    // copy string into another variable
    char s[5] = "OMAW";
    char hold[5] = "";
    printf("%s\n", s);
    // assign all s[i] into hold[i]
    for (int i = 0; i < 4; i++)
    {
        hold[i] = s[i];
        printf("%c\n", s[i]);
    }
    // try to printout as %s with out loop
    printf("%s\n", hold);
    // this loop is print out correctly
    // for (int i = 0; i < 4; i++)
    // {
    //     printf("%c", hold[i]);
    // }
    return 0;
}