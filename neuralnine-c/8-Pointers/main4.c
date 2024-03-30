#include <stdio.h>

void function1() {
    printf("function 1\n");
}

void function2() {
    printf("function 2\n");
}

int main() {
    void(*myfunction)();
    myfunction = function1;
    myfunction();
    myfunction = function2;
    myfunction();

    return 0;
}