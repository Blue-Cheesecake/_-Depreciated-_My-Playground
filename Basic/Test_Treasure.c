#include <stdio.h>
#include <string.h>
#include <math.h>

void cal_direc(double *x, double *y, char *s, double val)
{
    // ! up
    if (strcmp(s, "N") == 0)
    {
        *y += val;
    }
    // ! down
    else if (strcmp(s, "S") == 0)
    {
        *y -= val;
    }
    // ! right
    else if (strcmp(s, "E") == 0)
    {
        *x += val;
    }
    // ! left
    else if (strcmp(s, "W") == 0)
    {
        *x -= val;
    }
    // ! up right
    else if (strcmp(s, "NE") == 0)
    {
        *x += val;
        *y += val;
    }
    // ! down right
    else if (strcmp(s, "SE") == 0)
    {
        *x += val;
        *y -= val;
    }
    // ! down left
    else if (strcmp(s, "SW") == 0)
    {
        *x -= val;
        *y -= val;
    }
    // ! up left
    else if (strcmp(s, "NW") == 0)
    {
        *x -= val;
        *y += val;
    }
}

void substring(char *s, char *var, int index, int len)
{
    int c = 0;
    while (c < len)
    {
        var[c] = s[index];
        c += 1;
        index += 1;
    }
    var[c] = '\0';
}

double turn_to_num(char *subN)
{
    double result = 0;
    double power_ten = strlen(subN) - 1;
    for (int i = 0; i < strlen(subN); i++)
    {
        // ? debug purpose
        // double multi_ten = pow(10, power_ten);
        // printf("multi:%.1f\n", multi_ten);
        result = result + ((subN[i] - '1' + 1) * pow(10, power_ten));
        power_ten -= 1;
    }

    return result;
}

double distance(double x, double y)
{
    return sqrt((pow(x, 2) + pow(y, 2)));
}

int main()
{
    // TODO separate substring int and direction
    // TODO turn substring int to real int

    int True = 1;
    double x = 0;
    double y = 0;
    while (True = 1)
    {
        char all[6];
        scanf("%s", all);
        if (strcmp(all, "*") == 0)
        {
            break;
        }
        int length = strlen(all);
        int length_num;
        int index_direction;
        int length_direction;
        // ! find index of direction
        for (int i = 0; i < length; i++)
        {
            if (all[i] >= 'A' && all[i] <= 'Z')
            {
                length_num = i;
                index_direction = i;
                length_direction = length - length_num;
                break;
            }
        }

        // ? debug purpose
        // printf("length_num:%d length_direction:%d index_direction:%d", length_num, length_direction, index_direction);

        char direction[3];
        char number[4];
        substring(all, direction, index_direction, length_direction);
        substring(all, number, 0, length_num);
        double real_val = turn_to_num(number);

        // ? debug purpose
        // printf("%s %s %.1f\n", number, direction, real_val);

        cal_direc(&x, &y, direction, real_val);
    }
    printf("%.3f %.3f\n", x, y);
    printf("%.3f", distance(x, y));
}
