#include <iostream>

int main() {
    int i;
    std::cin >> i;

    do {
        std::cout << i-- << std::endl;
    } while (i > 0);
    std::cout << i << std::endl;

    return 0;
}