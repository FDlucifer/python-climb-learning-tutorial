#include <iostream>
#include <string.h>

int main() {
    char text[16];
    char text2[200];
    std::cin >> text2;

    strcpy(text, text2);
    strcmp(text, text2);

    return 0;
}