// https://beta.programming.in.th/tasks/0037

#include <stdio.h>

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);
    int l, k, c;
    scanf("%d %d %d", &l, &k, &c);
    int field[n][m];
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &field[i][j]);
            sum += field[i][j];
        }
    }

    sum += (l * k * c);
    int result = sum / c;

    if (c * result < sum)
    {
        result += 1;
    }

    printf("%d", result);
    return 0;
}