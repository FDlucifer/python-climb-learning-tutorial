#include <stdio.h>
#include <stdlib.h>

int main() {
    char mystring[10];
    int i = 20;
    sprintf(mystring, "%d\n", i);
    printf("%s\n", mystring);

    return 0;
}