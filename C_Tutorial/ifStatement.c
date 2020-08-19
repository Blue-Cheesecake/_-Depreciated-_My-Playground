#include <stdio.h>

// if, else if, else statements

int main()
{
    // Using condition (if), the code that corresponding with (if) can be executed if that condition is Only -->True<--
    // By using relational and logical operators
    // Not quite sure if there are any operators to use with in C, But python, they exist
    int a = 10, b = 20;
    if ((a == 10) && (b == 20))
    {
        printf("a = 10 b = 20 True\n");
    }
    if ((a < 10) || (b >= 20))
    {
        printf("True\n");
    }
    return 0;
}
