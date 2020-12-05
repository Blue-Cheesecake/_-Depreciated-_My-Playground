#include <stdio.h>
#include <string.h>

void reverse(char *s, int right)
{
    int left = 0;
    while (left < right)
    {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left += 1;
        right -= 1;
    }
}

void reverseVowels(char *s)
{
    int len = strlen(s);
    char hold[len + 1];
    int hold_index = 0;
    for (int i = 0; i < len; i++)
    {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'u' || s[i] == 'o')
        {
            hold[hold_index] = s[i];
            hold_index += 1;
        }
    }
    reverse(hold, hold_index - 1);
    printf("%s  ", hold);
    hold_index = 0;
    for (int i = 0; i < len; i++)
    {
        if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'u' || s[i] == 'o')
        {
            s[i] = hold[hold_index];
            hold_index += 1;
        }
    }

    // return s;
}

int main()
{
    char t1[20] = "leetcode";
    reverseVowels(t1);
    printf("%s", t1);
}