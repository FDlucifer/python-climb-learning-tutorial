#include <stdio.h>

int main() {
    printf("%s", "fuck world\n");
    char mystring[10] = "hello";
    printf("%s\n", mystring);

    int a = (int) 'A';
    printf("%d\n", a);

    char b = (char) 66;
    printf("%c\n", b);

    char c = (char) 66.567;
    printf("%c\n", c);

    return 0;
}