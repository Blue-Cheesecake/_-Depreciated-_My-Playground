// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

#include <stdio.h>

int main()
{
    int size;
    scanf("%d", &size);
    int list[size];
    for (int i = 0; i < size; i++)
    {
        scanf("%d", &list[i]);
    }
    int max;
    for (int i = 0; i < size - 1; i++)
    {
        if (i == 0)
        {
            max = list[i];
        }
        for (int j = i + 1; j < size; j++)
        {
            int product = (list[i] - 1) * (list[j] - 1);
            if (product > max)
            {
                max = product;
            }
        }
    }
    printf("%d", max);
    return 0;
}