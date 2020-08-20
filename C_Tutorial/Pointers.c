#include <stdio.h>

// useful of pointer is to change value (In-place conception)
// objective of pointers might be to value of element
//  Q: if we change element in array by assign, is address equal to address by assign by pointer?
int main()
{
    int a = 20;
    char b[] = "string";
    int *ip;
    ip = &a;
    // address of file can be accessed by ampersand &
    // address of files are the same a == ip
    // means address of pointers that we assigned, values of pointers is the same of variable (because address is the same)
    printf("Access file a: %x\n", &a);
    printf("Access file pointA: %x\n", ip);
    printf("Access file b: %x\n", &b);
    // access Null if you dont have exact address to be assigned
    char *ipB = NULL;

    // Incrementing Pointer
    int length = 5;
    int array[] = {1, 2, 3, 4, 5};
    int *ptr;
    ptr = &array[0];
    for (int i = 0; i < length; i++)
    {
        printf("Address of var[%d] = %x\n", i, &array[i]);
        printf("Address of var[%d] = %x\n", i, ptr);
        // put * before pointer variablels to execute real values
        // but to access address of pointer variables there's no need to put & because pointer is the address of the files
        printf("Value of var[%d] = %d\n", i, array[i]);
        printf("Value of var[%d] = %d\n", i, *ptr);
        // move to the next location
        ptr++;
    }
    // Decrementing Pointer
    int *ptrA;
    ptrA = &array[length - 1];
    for (int j = length; j > 0; j--)
    {
        printf("Address of var[%d] = %x\n", j, ptrA);
        printf("Value of var[%d] = %d\n", j, *ptrA);
        // move to the previous location
        ptrA--;
    }
    // stored address element in array by using pointer
    int list[] = {100, 200, 300};
    // insert length of array into pointer
    int *ptrB[3];
    for (int q = 0; q < 3; q++)
    {
        ptrB[q] = &list[q];
    }
    // print Values of each element in array by pointer
    for (int w = 0; w < 3; w++)
    {
        printf("Value of list[%d] = %d\n", w, *ptrB[w]);
    }
    // pointer can be defined any of types, but you need to declare type correctly (may be a string, float,unsigned etc.) (I most likely used integer for examples)
    return 0;
}