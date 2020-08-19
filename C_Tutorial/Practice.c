#include <stdio.h>

double average(int array[], int len)
{
    double sigma = 0;
    double ret;
    for (int i = 0; i < len; i++)
    {
        sigma += array[i];
    }
    return sigma / len;
}

int main()
{
    int Array[5] = {1000, 2, 3, 17, 50};
    double avg = average(Array, 5);
    printf("%.2f", avg);
    return 0;
}