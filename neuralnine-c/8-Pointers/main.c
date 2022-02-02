#include <stdio.h>

int main() {
    int a = 10;
    int b = 20;
    char c = 'A';
    int d = 20;

    printf("%p\n", &a);
    printf("%p\n", &b);
    printf("%p\n", &c);
    printf("%p\n", &d);

    return 0;
}