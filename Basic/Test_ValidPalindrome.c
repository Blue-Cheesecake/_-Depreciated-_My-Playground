#include <stdbool.h>

bool isPalindrome(char *s)
{
    if (strlen(s) == 0)
    {
        return true;
    }
    // TODO clean the special word & turn into upper or lower
    // ! reverse as a palindrome
    // TODO check if it eaual or not
    int length = strlen(s);
    char clean[length];
    int indexClean = 0;
    for (int i = 0; i < strlen(s); i++)
    {
        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z') || (s[i] >= '0' && s[i] <= '9'))
        {
            if (s[i] >= 'A' && s[i] <= 'Z')
            {
                s[i] += 32;
            }
            clean[indexClean] = s[i];
            indexClean += 1;
        }
    }
    clean[indexClean] = '\0';
    // ! assign in reverse
    char reverse[length];
    strcpy(reverse, clean);
    int left = 0;
    int right = strlen(clean) - 1;
    while (left < right)
    {
        char temp = reverse[left];
        reverse[left] = reverse[right];
        reverse[right] = temp;

        left += 1;
        right -= 1;
    }
    if (strcmp(clean, reverse) == 0)
    {
        return true;
    }
    return false;
    // printf("%s %s", clean, reverse);
}
