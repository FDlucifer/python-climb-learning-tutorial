#include <iostream>

int main() {
    int a = 10;

    int *ptr = &a;

    std::cout << ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;
    std::cout << ++ptr << std::endl;

    *ptr = 20;
    std::cout << a << std::endl;

    return 0;
}