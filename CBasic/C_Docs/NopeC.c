#include <stdio.h>

int main()
{
    
    // how to compare the original and changed array
    int array[5] = {1, 2, 3, 4, 5};
    // can not copy array
    int hold[5] = array;
    for (int i = 0; i < 5; i++)
    {
        printf("Value of array[%d] %d\n", i, array[i]);
        // changed
        printf("Value of array[%d] %d\n", i, hold[i]);
    }
    return 0;
}