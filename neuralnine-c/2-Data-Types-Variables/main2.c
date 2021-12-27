#include <stdio.h>
#include <limits.h>
#include <float.h>

int main() {
    unsigned char c1 = 'A';
    char c2 = 90;

    printf("%d\n", c1);
    printf("%d\n", c2);

    printf("%c\n", c1);
    printf("%c\n", c2);

    printf("%ld\n", sizeof(c1));
    printf("MAX OF CAHR: %u\n", UCHAR_MAX);

    return 0;
}