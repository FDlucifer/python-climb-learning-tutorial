#include <stdio.h>
#include <limits.h>

int main() {
    int a = 10;
    int b = 20;
    int c = 30;

    printf("%d + %d = %d\n", a, b, c);
    printf("%ld\n", sizeof(a));

    short d = 500;
    printf("%d\n", d);
    printf("%ld\n", sizeof(d));

    printf("INT MAX VALUE: %d\n", INT_MAX);
    printf("INT MIN VALUE: %d\n", INT_MIN);

    printf("SHORT MAX VALUE: %d\n", SHRT_MAX);
    printf("SHORT MIN VALUE: %d\n", SHRT_MIN);

    long e = 412341234123;
    long long f = 345124378572834578;
    printf("%ld\n", e);
    printf("%lld\n", f);
    printf("size long: %ld\n", sizeof(e));
    printf("size long long: %ld\n", sizeof(f));

    printf("LONG MAX VALUE: %ld\n", LONG_MAX);
    printf("LONG LONG MAX VALUE: %lld\n", LLONG_MAX);

    unsigned long int g = 3413412315213452443;
    printf("%lu\n", g);
    printf("UNSIGNED LONG LONG MAX: %llu\n", ULLONG_MAX);

    return 0;
}