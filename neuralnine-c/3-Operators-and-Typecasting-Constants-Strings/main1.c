#include <stdio.h>

int main() {
    int a = 10;
    printf("%d\n", a);

    a = 20;
    printf("%d\n", a);

    const float PI = 3.14159265;
    const char NEWLINE = '\n';

    printf("my favorite number is %.5f%c", PI, NEWLINE);

    return 0;
}