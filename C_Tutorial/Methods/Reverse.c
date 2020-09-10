#include <stdio.h>

void recursinInPlace(int *s, int left, int right)
{
    //  implement recursive function which receives two pointers, left and right, as arguments.
    //  Base case: if left >= right, do nothing.
    //  Otherwise, swap s[left] and s[right] and call helper(left + 1, right - 1).
    // To solve the problem, passing the head and tail indexes as arguments: return helper(0, len(s) - 1).
    if (left >= right)
    {
        // pass
    }
    else
    {
        // swap
        int temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        recursinInPlace(s, left + 1, right - 1);
    }
}

int twoPointersIteration(int *s, int sSize)
{
    // initial left = the first index, right = the last index
    int left = 0;
    int right = sSize - 1;
    while (left < right)
    {
        // swap
        int temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        // move to the next index
        left += 1;
        right -= 1;
    }
}

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
    // separate in case odd and even
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