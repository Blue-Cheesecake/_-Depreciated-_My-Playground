#include <stdio.h>
#include <string.h>

void rotate_to_right(char *s, int index, int length)
{
    for (int i = length; i > index; i--)
    {
        s[i] = s[i - 1];
    }
}

void defangIPaddr(char *address)
{
    int length = strlen(address);
    int i = 0;
    while (i < length)
    {
        if (address[i] == '.')
        {
            rotate_to_right(address, i, length);
            address[i] = '[';
            rotate_to_right(address, i + 1, length + 1);
            address[i + 2] = ']';
            i += 2;
            length += 2;
        }
        i += 1;
    }
}

int main()
{

    char address[10001];
    scanf("%s", &address);
    defangIPaddr(address);
    printf("%s", address);
    return 0;
}