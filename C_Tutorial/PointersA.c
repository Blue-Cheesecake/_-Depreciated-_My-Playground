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
    // do not forget to put & before call void function (only variables that type of them are not array)
    ChangeValue(&value1);
    printf("Before change: %d\n", value1);

    int list[5] = {1000, 2, 3, 17, 50};
    // passing array into function
    // In array, you don't need to put & before array argument
    double result = average(list, 5);
    printf("%.2f\n", result);

    // There may be a situation when we want to maintain an array,which can store pointers to an int or char or any other data type available. Following is the declaration of an array of pointers to an integer
    const int MaxSize = 4;
    int tuple[] = {6, 7, 8, 9};
    // define pointer to store array
    int *point[MaxSize];
    for (int i = 0; i < MaxSize; i++)
    {
        // assign array[i] into pointer
        // do not forget & before variable that you want to store to refer address of variable
        point[i] = &tuple[i];
    }
    // print out the real value of pointer of array by using loop
    for (int j = 0; j < MaxSize; j++)
    {
        // do not forget * before pointer to access the real value of each pointers
        printf("%d ", *point[j]);
        // 6 7 8 9
    }

    return 0;
}