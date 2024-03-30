#include <stdio.h>
#include <limits.h>
#include <float.h>
#include <stdbool.h>

int main() {
    bool b = true;
    printf("%d\n", b);
    printf("%ld\n", sizeof(b));

    long double ld = 10.21;
    printf("size of ld: %ld\n", sizeof(ld));

    return 0;
}