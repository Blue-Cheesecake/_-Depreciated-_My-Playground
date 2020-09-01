#include <stdio.h>

// from int(reversed(len(str(n))))
int reversedLenStr(int num)
{
    int rev_num = 0;
    while (num > 0)
    {
        rev_num = rev_num * 10 + num % 10;
        num = num / 10;
    }
    return rev_num;
}

int powerd(int num, int k)
{
    int result = 1;
    for (int i = 1; i < k + 1; i++)
    {
        result = result * num;
    }
    return result;
}

// dictionary digits
void get(int num)
{
    if (num == 1)
    {
        printf("one ");
    }
    else if (num == 2)
    {
        printf("two ");
    }
    else if (num == 3)
    {
        printf("three ");
    }
    else if (num == 4)
    {
        printf("four ");
    }
    else if (num == 5)
    {
        printf("five ");
    }
    else if (num == 6)
    {
        printf("six ");
    }
    else if (num == 7)
    {
        printf("seven ");
    }
    else if (num == 8)
    {
        printf("eight ");
    }
    else if (num == 9)
    {
        printf("nine ");
    }
    else if (num == 0)
    {
        printf("zero ");
    }
}

void printDidits(int num)
{
    num = reversedLenStr(num);
    int i = 1;
    while (num > 0)
    {
        int rev = num % (powerd(10, i));
        get(reversedLenStr(rev));
        num -= rev;
        i += 1;
    }
}
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
    // this process only works well if the last digit is not 0
    printDidits(6432);
    printf("\n");
    printDidits(21045);
    printf("\n");
    printDidits(1001);

    return 0;
}