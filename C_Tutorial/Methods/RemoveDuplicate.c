#include <stdio.h>
/* concept --> 
for i in range len origin
    if origin[i] not in  hold
        add origin[i] into hold
*/
// In C might be a little bit complex
int main()
{
    // expected output is 1 2 0 3 4 5 6 7 8
    int array[] = {1, 2, 0, 2, 3, 4, 5, 6, 7, 7, 0, 8};
    int size = 12;
    // maximum size of hold must not more exceed length of array
    char hold[12] = {};
    // define all element in hold = NULL
    for (int first = 0; first < 12; first++)
    {
        hold[first] = 'N';
    }
    for (int i = 0; i < size; i++)
    {
        // if array[i] not in hold --> add
        int add = 1;
        for (int j = 0; j < size; j++)
        {
            if (array[i] == hold[j])
            {
                add = 0;
                break;
            }
        }
        if (add == 1)
        {
            for (int k = 0; k < size; k++)
            {
                if (hold[k] == 'N')
                {
                    hold[k] = array[i];
                    break;
                }
            }
        }
    }

    for (int element = 0; element < size; element++)
    {
        if (hold[element] != 'N')
        {
            printf("%d ", hold[element]);
        }
    }

    return 0;
}