#include <stdio.h>
#include <stdbool.h>

int main() {
    int choice;

    printf("enter a number: ");
    scanf("%d", &choice);

    if (true) {
        printf("this is always be executed!\n");
    }

    switch (10) {
        case 10:
            printf("test");
            break;
    }
    return 0;
}