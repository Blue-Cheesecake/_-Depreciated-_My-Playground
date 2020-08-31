#include <stdio.h>

// separate it into half
void reverse(int *list, int n)
{
    // hold back half of array
    int hold[n / 2];
    for (int i = 0; i < n / 2; i++)
    {
        hold[i] = list[i];
    }

    int index = n - 1;
    for (int j = 0; j <= n / 2; j++)
    {
        list[j] = list[index];
        index -= 1;
    }
    index = n / 2;
    int eo;
    if (n % 2 == 0)
    {
        eo = n / 2;
    }
    else
    {
        eo = n / 2 + 1;
    }
    for (int l = eo; l < n; l++)
    {
        list[l] = hold[index - 1];
        index -= 1;
    }
}

int main()
{
    int arr[6] = {1, 2, 3, 4, 5, 6};
    reverse(arr, 6);
    for (int i = 0; i < 6; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
    int arrA[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    reverse(arrA, 9);
    for (int j = 0; j < 9; j++)
    {
        printf("%d ", arrA[j]);
    }
    return 0;
}