#include <stdio.h>

int sum(int *arr, int from, int to)
{
    int out = 0;
    while (from <= to)
    {
        out += arr[from];
        from += 1;
    }
    return out;
}

int main()
{
    int t1[5] = {1, 2, 3, 4, 5};
    int ret = sum(t1, 1, 4);
    printf("%d ", ret);
    return 0;
}