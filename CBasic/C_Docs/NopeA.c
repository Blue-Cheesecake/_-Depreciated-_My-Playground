#include <stdio.h>
#include <stdlib.h>


char PassOrNot(int values)
{
    if (values > 60)
    {
        return 'P';
    }
    else
    {
        return 'F';
    }

}

int main()
{
    char Key= PassOrNot(20);
    printf("%c", Key);
    return 0;
}