#include <stdio.h>
#include <stdbool.h>

int main() {
    char choice;

    printf("enter a number: ");
    scanf("%c", &choice);

    switch (choice) {
        case 'A':
            printf("you selected option A\n");
            break;
        case 'B':
            printf("you selected option B\n");
            break;
        default:
            printf("please select option A or B\n");
            break;
    }

    bool mycondition = true;
    printf(mycondition ? "True\n" : "False\n");
    return 0;
}