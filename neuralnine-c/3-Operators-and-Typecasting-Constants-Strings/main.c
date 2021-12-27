#include <stdio.h>

int main() {
    int x = 50;
    int y = 20;
    int z = 10;

    printf("%d\n", ((x < y) && (y < z)));
    printf("%d\n", ((x < y) || (y < z)));
    printf("%d\n", !(x < y));
    printf("%d\n", 23 & 20);

    return 0;
}