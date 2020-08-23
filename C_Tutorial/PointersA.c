#include <stdio.h>

// C  programming  language  allows  you  to  pass  a  pointer  to  a  function.  To  do  so,  simply declare the function parameter as a pointer type.
// Following  a  simple  example  where  we  pass  an  (types)  pointer  to  a  function  and change the value inside the function which reflects back in the calling function

void ChangeValue(int *parameter)
{
    *parameter = 20;
}

// The  function, which  can  accept  a  pointer,  can  also  accept  an  array

double average(int *array, int len)
{
    double sigma = 0;
    for (int i = 0; i < len; i++)
    {
        sigma += array[i];
    }
    return sigma / len;
}

int main()
{
    int value1 = 2;
    printf("After change: %d\n", value1);
    // now we change value1 to 20
    // do not forget to put & before call void function
    ChangeValue(&value1);
    printf("Before change: %d\n", value1);

    int list[5] = {1000, 2, 3, 17, 50};
    // passing array into function
    // In array, you don't need to put & before array argument
    double result = average(list, 5);
    printf("%.2f\n", result);
    return 0;
}