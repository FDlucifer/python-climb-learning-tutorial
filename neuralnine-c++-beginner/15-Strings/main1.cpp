#include <iostream>
#include <string.h>

int main() {
    char text[4] = "Hey";
    std::cout << sizeof(text) << std::endl;
    std::cout << strlen(text) << std::endl;

    return 0;
}