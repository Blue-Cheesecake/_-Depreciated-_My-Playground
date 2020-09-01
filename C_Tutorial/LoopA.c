#include <stdio.h>

// print n-th fibonacci number
// sequence = 0 1 1 2 3 5 8 13 21 ....
int fibonacci(int n)
{
    int previous = 1;
    int current = 1;
    if (n <= 1)
    {
        return n;
    }
    else
    {
        for (int i = 3; i < n; i++)
        {
            int temp = current;
            current += previous;
            previous = temp;
        }
    }
    return current;
}

int main()
{
    printf("%d ", fibonacci(9));
    return 0;
}