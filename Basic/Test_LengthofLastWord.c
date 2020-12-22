// https://leetcode.com/problems/length-of-last-word/

#include <string.h>

int lengthOfLastWord(char *s)
{
    if (strcmp(s, " ") == 0)
    {
        return 0;
    }
    char *token = strtok(s, " ");
    char lastStr[10001];
    while (token != NULL)
    {
        // printf("%s\n", token);
        strcpy(lastStr, token);
        token = strtok(NULL, " ");
    }
    return strlen(lastStr) - 1;
}
