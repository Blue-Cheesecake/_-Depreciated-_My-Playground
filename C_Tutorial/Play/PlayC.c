#include <stdio.h>

int main()
{
    // optional
    int array = {1, 2, 3, 4, 5};
    int size, element, posi;
    element = 8;
    posi = size;
    // make room for new array element
    for (int i = size; i >= posi; i--)
    {
        array[i] = array[i - 1];
    }
    array[posi - 1] = element;
    size++;
}