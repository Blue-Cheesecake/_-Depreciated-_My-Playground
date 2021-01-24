/*  -----  Please fill in your information in this comment block -----  
   Student ID: 
   Fullname: 
   Section: 
---------------------------------------------------------------------- */

#include <stdio.h>

void scan_arr(int *arr1, int n1)
{
    int i;
    for (i = 0; i < n1; i++)
    {
        scanf("%d", &arr1[i]);
    }
}

void print_arr(int *arr1, int n1, int id)
{
    printf("arr%d: ", id);
    int i;
    for (i = 0; i < n1; i++)
    {
        printf("%d ", arr1[i]);
    }
    printf("\n");
}

void swap(int *max, int *last)
{
    int temp = *max;
    *max = *last;
    *last = temp;
}

int some(int *arr1, int n1, int *p_max)
{
    p_max = &arr1[0];
    int i;
    for (i = 1; i < n1; i++)
    {
        if (*p_max < arr1[i])
        {
            // p_max = &arr1[i];
            return i;
        }
    }
    return -1;
}

int main()
{
    /*
        Ask a user to input 2 integer arrays
    */
    int n1;
    scanf("%d", &n1);
    int arr1[n1];

    int i;
    scan_arr(arr1, n1);

    int n2;
    scanf("%d", &n2);
    int arr2[n2];
    scan_arr(arr2, n2);
    /*
        Print the values of the arrays
    */
    printf("Before swap min and max\n");
    print_arr(arr1, n1, 1);
    print_arr(arr2, n2, 2);

    /*
        For each array:
          - Swap the maximum value with the last element using a pointer
          - Swap the minimum value with the first element using a pointer
    */
    int *p_max, *p_min, *p_first, *p_last;
    // int temp;

    // Arrar 1
    p_max = &arr1[0];
    p_last = &arr1[n1 - 1];
    // int hold = some(arr1, n1, p_max);
    // if (hold != -1)
    // {
    //     p_max = &arr1[hold];
    // }

    for (i = 1; i < n1; i++)
    {
        if (*p_max < arr1[i])
        {
            p_max = &arr1[i];
        }
    }

    swap(p_max, p_last);

    p_min = &arr1[0];
    p_first = &arr1[0];

    for (i = 1; i < n1; i++)
    {
        if (*p_min > arr1[i])
        {
            p_min = &arr1[i];
        }
    }

    swap(p_min, p_first);
    // Arrar 2
    p_max = &arr2[0];
    p_last = &arr2[n2 - 1];
    // if (some(arr2, n2, p_max) != -1)
    // {
    //     p_max = &arr2[some(arr2, n2, p_max)];
    // }
    // some(arr2, n2, p_max);
    for (i = 1; i < n2; i++)
    {
        if (*p_max < arr2[i])
        {
            p_max = &arr2[i];
        }
    }

    swap(p_max, p_last);

    p_min = &arr2[0];
    p_first = &arr2[0];
    // some2(arr2, n2, p_min);
    for (i = 1; i < n2; i++)
    {
        if (*p_min > arr2[i])
        {
            p_min = &arr2[i];
        }
    }

    swap(p_min, p_first);

    /*
        Print the values of the arrays
    */
    printf("After swap min and max\n");
    print_arr(arr1, n1, 1);
    print_arr(arr2, n2, 2);

    return 0;
}