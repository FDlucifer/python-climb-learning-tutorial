#include <iostream>

int main() {

    // arithmetic operators
    int a = 10, b = 2;
    std::cout << a * b + 40 << std::endl;

    a = a + 10;
    std::cout << ++a << std::endl;
    std::cout << a++ << std::endl;

    // comparison operators (Relational)
    std::cout << (a > b) << std::endl;
    std::cout << (a <= b) << std::endl;

    // logical operators
    std::cout << ((a < b) || (a > 5)) << std::endl;

    // bitwise operator
    
    return 0;
}