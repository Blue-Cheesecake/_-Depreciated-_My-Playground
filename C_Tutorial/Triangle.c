#include <stdio.h>

int main()
{
    int startEle = 1;
    int givenN = 25;
    int expectLen = 1;
    while (startEle < givenN)
    {
        if (startEle + expectLen > givenN)
        {
            break;
        }
        int count = 0;
        while (count < expectLen)
        {
            printf("%d ", startEle);
            count += 1;
            startEle += 1;
        }
        printf("\n");
        expectLen += 1;
    }

    return 0;
}