#include <stdio.h>
#include <stdlib.h>

int main()
{
    int plus;
    int a = 10;
    int b = 20;
    printf("plus a + b = %d\n", func(a, b));
    printf("%d %d\n", a, b);
    // do not forget & in parameters and * in void function
    swap(&a, &b);
    printf("%d %d\n", a, b);
    return 0;
}

int func(int num1, int num2)
{
    return num1 + num2;
}

// in-place methods(you need to put * before var (pass value by ref))
// * means accessing to address and change them (pointer)
void swap(int *num1, int *num2)
{
    int temp = *num1;
    *num1 = *num2;
    *num2 = temp;
}

// void means you dont want anything to return (In-place)
// another might return result