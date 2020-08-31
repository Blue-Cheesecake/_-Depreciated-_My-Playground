#include <stdio.h>

int powerd(int num, int k)
{
    int result = 1;
    for (int i = 1; i < k + 1; i++)
    {
        result = result * num;
    }
    return result;
}

// lenStr means --> len(str(int)) in python
int lenStr(int x)
{
    if (x == 0)
    {
        return 1;
    }
    int i = 1;
    int count = 0;
    while (x > 0)
    {
        count += 1;
        x -= (x % (powerd(10, i)));
        i += 1;
    }
    return count;
}

int main()
{
    printf("%d %d %d", lenStr(95436), lenStr(1234), lenStr(54678893));
    return 0;
}