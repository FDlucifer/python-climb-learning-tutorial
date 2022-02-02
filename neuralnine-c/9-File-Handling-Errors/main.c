#include <stdio.h>

int main() {
    FILE *fileptr = fopen("test.txt", "w");
    fprintf(fileptr, "hello world!\n");
    fflush(fileptr);
    fclose(fileptr);

    FILE *fileptr2 = fopen("test.txt", "r");
    char c;
    while ((c = fgetc(fileptr2)) != EOF) {
        printf("%c", c);
    }
    fclose(fileptr2);

    FILE *fileptr4 = fopen("test.txt", "a");
    fprintf(fileptr4, "new line\n");
    fclose(fileptr4);

    FILE *fileptr3 = fopen("test.txt", "r");
    char currentline[500];
    while (fgets(currentline, 500, fileptr3) != NULL) {
        printf("%s", currentline);
    }
    fclose(fileptr3);

    return 0;
}