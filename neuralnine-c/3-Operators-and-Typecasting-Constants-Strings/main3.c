#include <stdio.h>
#include <stdlib.h>

int main() {
    char mystring[10] = "1788";
    int i = atoi(mystring);
    printf("%d\n", i + 10);

    float f = atof(mystring);
    printf("%.3f\n", f);

    return 0;
}