#include <stdio.h>
#include <stdbool.h>

int main() {
    int choice;

    printf("enter a number: ");
    scanf("%d", &choice);

    if (choice < 100) {
        printf("your input is less than a hundred!\n");
        if (choice < 50) {
            printf("your input is alse less than 50!\n");
        }
    }
    if (choice % 2 == 0) {
        printf("your number is even!\n");
    } else {
        printf("your number is odd!\n");
    }

    return 0;
}