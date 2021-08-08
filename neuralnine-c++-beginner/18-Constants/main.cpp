#include <iostream>

int main() {
    int a = 10;
    int b = 20;

    const int *p1 = &a;
    int* const p2 = &a;

    *p2 = 20;
    std::cout << a << std::endl;

    return 0;
}