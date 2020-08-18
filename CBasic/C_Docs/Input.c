#include <stdio.h>

float BasicAverage(int n1, int n2, int n3)
{
    float sum = 0;
    sum = n1 + n2 + n3;
    return sum / 3;
}

int main()
{
    float i, j, k;
    // do not forget &
    scanf("%f %f %f", &i, &j, &k);
    // .[i]f --> round()
    printf("%f\"", BasicAverage(i, j, k));
    // char a[10], b[10], c[10];
    // scanf("%s %s %s", a, b, c);
    // printf("%s %s %s\n", a, b, c);
    // char MaName[20];
    // scanf("%s", &MaName);
    // for (int i = 0; i < 20; i++)
    // {
    //     printf("%d ", MaName[i]);
    // }

    return 0;
}