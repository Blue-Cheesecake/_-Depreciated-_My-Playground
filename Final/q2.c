/*  -----  Please fill in your information in this comment block -----  
   Student ID: 6388073
   Fullname: Sinut Wattnarporn
   Section: 3
---------------------------------------------------------------------- */

/*  ===== Put your code here ===== */

#include <stdio.h>
#include <string.h>

void reverse(char *s)
{
    int left = 0;
    int right = strlen(s) - 1;
    while (left < right)
    {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;

        left += 1;
        right -= 1;
    }
}

int main()
{
    char input[101];
    fgets(input, 101, stdin);
    char clean[101];
    int index = 0;
    for (int i = 0; i < strlen(input); i++)
    {
        if (input[i] >= 'A' && input[i] <= 'Z')
        {
            input[i] += 32;
        }
        if (input[i] >= 'a' && input[i] <= 'z')
        {
            clean[index] = input[i];
            index += 1;
        }
    }
    clean[index] = '\0';
    char reve[101];
    strcpy(reve, clean);
    reverse(reve);

    if (strcmp(reve, clean) == 0)
    {
        printf("Palindrome");
        return 0;
    }
    else
    {
        printf("Not palindrome");
    }
}