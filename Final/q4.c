/*  -----  Please fill in your information in this comment block -----  
   Student ID: 6388073
   Fullname: Sinut Wattnarporn
   Section: 3
---------------------------------------------------------------------- */

/*  ===== Put your code here ===== */

#include <stdio.h>
#include <string.h>

void pop(char *s, int index)
{
    for (int i = index; i < strlen(s); i++)
    {
        s[i] = s[i + 1];
    }
}

int main()
{
    char input[51];
    fgets(input, 50, stdin);
    char *pos;
    if ((pos = strchr(input, '\n')) != NULL)
        *pos = '\0';

    int i = 0;
    int len = strlen(input);
    int count = 0;
    while (i < len)
    {
        char check = input[i];
        int j = i + 1;
        while (j < len)
        {
            char compare = input[j];
            if (check == compare)
            {
                pop(input, j);
                len -= 1;
                count += 1;
            }
            else
            {
                j += 1;
            }
        }
        i += 1;
    }

    printf("%s %d", input, count);
}