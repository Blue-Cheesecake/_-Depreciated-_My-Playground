// ! https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

#include <stdio.h>
#include <string.h>

void substring(char *s, char *hold, int index, int length)
{
    int c = 0;
    while (c < length)
    {
        hold[c] = s[index + c];
        c += 1;
    }
    hold[c] = '\0';
}

int isPrefixOfWord(char *sentence, char *searchWord)
{
    // ! extract each word
    int th = 0;
    int count_each_word = 1;
    int minimum = strlen(sentence);
    for (int i = 0; i < strlen(sentence); i++)
    {
        if (sentence[i] == ' ')
        {
            count_each_word += 1;
        }
    }

    int index = 0;
    for (int i = 0; i < count_each_word; i++)
    {
        int length_each = 0;
        for (int j = index; j < strlen(sentence); j++)
        {
            if (sentence[j] != ' ')
            {
                // printf("%c", sentence[j]);
                length_each += 1;
                index += 1;
            }
            else
            {
                index += 1;
                break;
            }
        }
        // printf(" %d %d", length_each, index);
        // printf("\n");
        // printf("%d %d\n", index, index - length_each - 1);
        char substr[11];
        int actual_index;
        if (index == strlen(sentence))
        {
            actual_index = index - length_each;
        }
        else
        {
            actual_index = index - length_each - 1;
        }
        substring(sentence, substr, actual_index, length_each);

        // ! printf("%s\n", all_word[i].string);

        if (strlen(substr) >= strlen(searchWord))
        {
            char sub_of_substr[11];
            substring(substr, sub_of_substr, 0, strlen(searchWord));
            // ! printf("%s %s\n", sub_of_substr, searchWord);
            if (strcmp(sub_of_substr, searchWord) == 0)
            {
                if (i + 1 < minimum)
                {
                    minimum = i + 1;
                }
            }
        }
    }
    if (minimum == strlen(sentence))
    {
        return -1;
    }

    return minimum;
}
