// https://beta.programming.in.th/tasks

#include <stdio.h>
#include <string.h>

void sort(int *list, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = i + 1; j < size; j++)
        {
            if (list[i] > list[j])
            {
                int temp = list[i];
                list[i] = list[j];
                list[j] = temp;
            }
        }
    }
}

int main()
{
    // TODO sort A B C
    // TODO print in given order
    int abc[3];
    for (int i = 0; i < 3; i++)
    {
        scanf("%d ", &abc[i]);
    }
    sort(abc, 3);
    char order[4];
    scanf("%s", order);
    for (int i = 0; i < 3; i++)
    {
        if (order[i] == 'A')
        {
            printf("%d", abc[0]);
        }
        else if (order[i] == 'B')
        {
            printf("%d", abc[1]);
        }
        else if (order[i] == 'C')
        {
            printf("%d", abc[2]);
        }
        if (i != 2)
        {
            printf(" ");
        }
    }
}