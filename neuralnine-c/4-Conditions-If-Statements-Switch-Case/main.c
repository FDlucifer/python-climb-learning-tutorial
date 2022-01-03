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
    } else if (choice < 200) {
        printf("your input is between 100 and 200!\n");
    } else {
        printf("your input is not less than a hundred!\n");
    }

    return 0;
}
