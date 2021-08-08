#include <iostream>

enum Color {
    RED, GREEN, BLUE, PURPLE, ORANGE
};

int main() {
    Color mycolor = PURPLE;

    std::cout << BLUE << std::endl;
    std::cout << ORANGE << std::endl;
    std::cout << mycolor << std::endl;
    return 0;
}