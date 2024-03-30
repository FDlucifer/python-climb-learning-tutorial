#include <iostream>

int main() {
    int a = 10;
    std::cout << &a << std::endl;

    int *myptr = &a;
    std::cout << *myptr << std::endl;

    *myptr = 20;
    std::cout << a << std::endl;

    return 0;
}