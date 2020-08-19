#include <stdio.h>

// data and variable types, declaration and definition
// arithmetic and relational operators are the same as python
// logic operators >> and = &&, or = ||, not = !

// function declaration
int func1();

int main()
{

    printf("Hello world\n");
    // check strorage size of data type
    printf("Storage size of int : %d \n", sizeof(int));

    // variable types
    // variable declaration
    char a;
    int b;
    float c;
    double d;

    // actual initialization
    b = 10;
    c = 1.5;
    d = 2.32;
    int plus = b + c + d;
    float plusf = b + c + d;
    printf("Value of plus : %d or %f\n", plus, plusf);

    // function call
    int valueF = func1();

    // constants and literals
    // constants can not be fixed but not literals
    const double pi = 3.14;
    printf("Constant number of pi : %lf \n", pi);

    return 0;
}

// function definition
int func1()
{
    return 0;
}