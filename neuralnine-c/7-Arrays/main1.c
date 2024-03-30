#include <stdio.h>

int main() {
    int myarray[5] = {};
    int otherarray[10] = {};

    for (int i = 0; i < 15; i++) {
        myarray[i] = i * 10;
    }

    for (int i = 0; i < 5; i++) {
        printf("%d\n", myarray[i]);
    }

    for (int i = 0; i < 10; i++) {
        printf("%d\n", otherarray[i]);
    }
    return 0;
}