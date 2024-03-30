#include <iostream>

int main() {
    bool a = true;

    bool *ptr = &a;

    std::cout << ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;

    return 0;
}