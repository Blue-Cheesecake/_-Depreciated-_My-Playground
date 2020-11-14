// https://www.programming.in.th/task/rev2_problem.php?pid=1019

#include <stdio.h>
#include <string.h>

void substring(char *s, char *sub, int p, int l)
{
    int c = 0;

    while (c < l)
    {
        sub[c] = s[p + c];
        c++;
    }
    sub[c] = '\0';
}

void longestDNA(char *dna1, char *dna2)
{
    if (strlen(dna1) < strlen(dna2))
    {
        char temp[201];
        strcpy(temp, dna1);
        strcpy(dna1, dna2);
        strcpy(dna2, temp);
    }

    char result[201] = "";
    for (int idx_dna1 = 0; idx_dna1 < strlen(dna1) - 1; idx_dna1++)
    {
        char tempResult[201];
        int idx_dna2 = 0;
        while (idx_dna2 < strlen(dna2) - 1)
        {
            int len_to_cmp = 2;
            char compareDna1[201];
            char compareDna2[201];
            // printf("idx_dna2 --> %d len --> %d\n", idx_dna2, len_to_cmp);
            substring(dna1, compareDna1, idx_dna1, len_to_cmp);
            substring(dna2, compareDna2, idx_dna2, len_to_cmp);
            // printf("%s ", compareDna1);
            // printf("%s ", compareDna2);
            // printf("%d \n", strcmp(compareDna1, compareDna2));
            while (strcmp(compareDna1, compareDna2) == 0 && len_to_cmp <= strlen(dna2))
            {
                strcpy(tempResult, compareDna1);
                len_to_cmp += 1;
                char hold1[201];
                char hold2[201];
                substring(dna1, hold1, idx_dna1, len_to_cmp);
                substring(dna2, hold2, idx_dna2, len_to_cmp);
                strcpy(compareDna1, hold1);
                strcpy(compareDna2, hold2);
                if (strlen(tempResult) > strlen(result))
                {
                    strcpy(result, tempResult);
                    // printf("%s", result);
                }
                if (len_to_cmp > strlen(dna2))
                {
                    break;
                }
            }
            idx_dna2 += 1;
        }
    }
    printf("%s", result);
}

int main()
{
    char dna1[201];
    char dna2[202];
    scanf("%s", dna1);
    scanf("%s", dna2);
    longestDNA(dna1, dna2);
    // char dna1_1[200] = "CTGAATCTACTGCTATTGCAA";
    // char dna2_1[200] = "AAAACTGCTACCGGT";
    // longestDNA(dna1_1, dna2_1);
    // printf("\n");
    // char dna1_2[200] = "AAACTGCACACTGTGTGGGGGACTGG";
    // char dna2_2[200] = "ACTGTGTGTGACACTGACAGTGACTGGGACTGAAGGGGGGG";
    // longestDNA(dna1_2, dna2_2);
    return 0;
}
