#include <iostream>

int main() {
    int i;
    std::cin >> i;

    while (i > 0) {
        std::cout << i-- << std::endl;
    }
    std::cout << i << std::endl;

    return 0;
}