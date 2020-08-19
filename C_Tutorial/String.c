#include <stdio.h>

int main()
{

    char s[5] = "OMAW";
    char hold[5] = "";
    printf("%s\n", s);
    // assign all s[i] into hold[i]
    for (int i = 0; i < 4; i++)
    {
        hold[i] = s[i];
        printf("%c\n", s[i]);
    }
    // expect OMAW
    // but instead OMAWOMAW is executed
    // try to printout as %s with out loop
    printf("%s\n", hold);
    // this loop is print out correctly
    // for (int i = 0; i < 4; i++)
    // {
    //     printf("%c", hold[i]);
    // }
    return 0;
}