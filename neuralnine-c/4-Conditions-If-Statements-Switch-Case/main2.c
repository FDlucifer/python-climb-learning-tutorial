#include <stdio.h>
#include <stdbool.h>

int main() {
    int choice;

    printf("enter a number: ");
    scanf("%d", &choice);

    switch (choice) {
        case 100:
            printf("one hundred!\n");
        case 10:
            printf("ten!\n");
            break;

        default:
            printf("not ten and not one hundred!\n");
            break;
    }
    return 0;
}