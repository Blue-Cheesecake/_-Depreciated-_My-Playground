#include <stdio.h>

// Scope rules of C aare divided in 2 scopes
// 1. Local  2. Global
// Variables with Local, means varibles that can be used must be in function itself or initilize with global
// Variables with Global, means these variables can be used in any function
// Global variable should be located on the top of any fucntion

// example of global variables
int varG1 = 5;
float varG2 = 20;
// means these variables varG1 and varG2 can be used in any function

int SomeFunction()
{
    // we can use varG1 and varG2 without define newly
    float i = varG1 + varG2;
    // i = 25
}

int main()
{
    // we can not use i from SomeFunction because it's local varible. Somethings like this:
    // int j = i + varG1;
    // it will cause error because i is not defined yet but varG1 can be used
    return 0;
}
