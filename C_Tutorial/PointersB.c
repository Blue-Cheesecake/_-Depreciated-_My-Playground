#include <stdio.h>

// --> Return pointer from functions <--

int main()
{
    // --> Pointer to Pointer <--
    // A pointer to a pointer is a form of multiple indirection, or a chain of pointers.
    // Normally, a pointer contains the address of a variable. When we define a pointer to a pointer, the first pointer  contains  the  address  of  the  second  pointer,  which  points  to  the  location  that contains the actualvalue
    //  Pointer1 (address) --> Pointer2 (address) --> Variable (Value)
    int x = 333;
    int *p1;
    int **p2;
    // When a target value is indirectly pointed to by a pointer to a pointer, accessing that value requires that the asterisk operator be applied twice
    // take address of target
    p1 = &x;
    // take address of pointer
    p2 = &p1;
    printf("x = %d p1 = %d p2 = %d", x, *p1, **p2);
    return 0;
}