#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

int main() {
    FILE *fp = fopen("noexistent.txt", "r");
    if (fp == NULL) {
        perror("Error");
        printf("%d\n", errno);
    } else {
        char c;
        while ((c = fgetc(fp)) != EOF) {
            printf("%c", c);
        }
    }

    int dividend = 20;
    int divisor = 0;

    if (divisor == 0) {
        exit(EXIT_FAILURE);
    }
    printf("%d\n", dividend / divisor);

    return 0;
}