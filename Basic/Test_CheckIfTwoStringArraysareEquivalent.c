#include <stdio.h>
#include <string.h>

struct words
{
    char word[101];
};

int main()
{
    int word1_size;
    scanf("%d", &word1_size);
    struct words word_1[word1_size];
    for (int i = 0; i < word1_size; i++)
    {
        scanf("%s", &word_1[i].word);
    }

    int word2_size;
    scanf("%d", &word2_size);
    struct words word_2[word1_size];
    for (int i = 0; i < word2_size; i++)
    {
        scanf("%s", &word_2[i].word);
    }

    char cmp_1[101] = "";
    for (int i = 0; i < word1_size; i++)
    {
        strcat(cmp_1, word_1[i].word);
    }

    char cmp_2[101] = "";
    for (int i = 0; i < word2_size; i++)
    {
        strcat(cmp_2, word_2[i].word);
    }

    if (strcmp(cmp_1, cmp_2) == 0)
    {
        printf("True");
    }
    else
    {
        printf("False");
    }
}