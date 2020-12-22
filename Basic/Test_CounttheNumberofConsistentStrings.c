// https://leetcode.com/problems/count-the-number-of-consistent-strings/

#include <string.h>

int countConsistentStrings(char *allowed, char **words, int wordsSize)
{
    int count = 0;
    for (int i = 0; i < wordsSize; i++)
    {
        char each_word[11];
        strcpy(each_word, words[i]);
        int all_in = 1;
        for (int j = 0; j < strlen(each_word); j++)
        {
            // ! check if each[j] in allowed or not
            // ! if in -> pass, else -> dont count
            int in = 0;
            for (int k = 0; k < strlen(allowed); k++)
            {
                if (each_word[j] == allowed[k])
                {
                    in = 1;
                    break;
                }
            }
            if (in == 0)
            {
                all_in = 0;
                break;
            }
        }
        if (all_in == 1)
        {
            count += 1;
        }
    }
    return count;
}
