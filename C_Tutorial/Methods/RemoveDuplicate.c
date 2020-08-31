#include <stdio.h>
/* concept --> 
for i in range len origin
    if origin[i] not in  hold
        add origin[i] into hold
assign hold element into original list
*/

// return new size
int removeDuplicate(int *list, int n)
{
    // try not to use sort method
    // In-place array in its original order
    // insert all element in hold to NULL
    int newSize = 0;
    int hold[n];
    for (int set = 0; set < n; set++)
    {
        hold[n] = 'N';
    }
    for (int i = 0; i < n; i++)
    {
        // if j not in hold --> add
        int add = 1;
        for (int j = 0; j < newSize; j++)
        {
            if (hold[j] == list[i])
            {
                add = 0;
            }
        }
        if (add == 1)
        {
            hold[newSize] = list[i];
            newSize += 1;
        }
    }
    // we got perfect element in hold
    // define all element in list == NULL
    for (int nu = 0; nu < newSize + 1; nu++)
    {
        list[nu] = hold[nu];
    }

    return newSize;
}

int main()
{
    // expected output is 1 2 0 3 4 5 6 7 8
    int array[12] = {1, 2, 0, 2, 3, 4, 5, 6, 7, 7, 0, 8};
    int size = 12;
    int new = removeDuplicate(array, size);
    for (int i = 0; i < new; i++)
    {
        printf("%d ", array[i]);
    }
    // expected output is 1 6 4 2 8 3
    int arrayA[10] = {1, 6, 4, 2, 6, 1, 8, 8, 3, 2};
    int newA = removeDuplicate(arrayA, 10);
    printf("\n");
    for (int j = 0; j < newA; j++)
    {
        printf("%d ", arrayA[j]);
    }

    return 0;
}