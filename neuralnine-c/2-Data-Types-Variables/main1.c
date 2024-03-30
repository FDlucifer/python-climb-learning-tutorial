#include <stdio.h>
#include <limits.h>
#include <float.h>

int main() {
    float f1 = 124321.567893456728;
    printf("%.20f\n", f1);
    printf("size of f1: %ld\n", sizeof(f1));

    double d1 = 123456.876534569876;
    printf("%.20f\n", d1);
    printf("size of d1: %ld\n", sizeof(d1));

    printf("MAX FLOAT: %f\n", FLT_MAX);
    printf("MAX DOUBLE: %f\n", DBL_MAX);

    return 0;
}