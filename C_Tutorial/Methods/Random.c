#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//  rand function generates a random number from 0 to RAND_MAX.
// With the help of rand () a number in range can be generated as
// num = (rand() % (upper – lower + 1)) + lower   (formular)

// numbers in range [lower, upper]
void RandomsNtimes(int lower, int upper, int count)
{
    int i;
    for (i = 0; i < count; i++)
    {
        int num = (rand() % (upper - lower + 1)) + lower;
        printf("%d ", num);
    }
}

// numbers in range [lower, upper]
int Random1times(int lower, int upper)
{
    int num = (rand() % (upper - lower + 1)) + lower;
    return num;
}

int main()
{
    // ------->    arbitary numbers     <-------
    int lower = 0, upper = 2, count = 1;
    // Use current time as
    // seed for random generator
    srand(time(0));
    return 0;
}