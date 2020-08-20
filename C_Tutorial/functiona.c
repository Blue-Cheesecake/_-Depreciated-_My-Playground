#include <stdio.h>

int max(int num1, int num2)
{
    int result;
    if (num1 > num2)
    {
        result = num1;
    }
    else
    {
        result = num2;
    }
    return result;
}

int min(int num1, int num2)
{
    int result;
    if (num1 < num2)
    {
        result = num1;
    }
    else
    {
        result = num2;
    }
    return result;
}

// how ever, C already has power function
int pow(int num, int k)
{
    int result = 1;
    for (int i = 1; i < k + 1; i++)
    {
        result = result * num;
    }
    return result;
}

int main()
{
    printf("Changed\n");
    int A = 10;
    int B = 20;
    int C = max(A, B);
    int D = min(A, B);
    int E = pow(2, 3);
    printf("%d %d %d %d\n", A, B, C, D);
    printf("Power : %d\n", E);
    return 0;
}

//return_type function_name(parameter list ){
// body of the function
// }