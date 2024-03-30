#include <stdio.h>

int main() {
    int numbers[100];
    int *first = numbers;
    for (int i = 0; i < 100; i++) {
        *(first + i) = i * 20;
    }

    for (int i = 0; i < 100; i++) {
        printf("%d\n", numbers[i]);
    }

    char c = 'A';
    printf("%s\n", &c);

    return 0;
}