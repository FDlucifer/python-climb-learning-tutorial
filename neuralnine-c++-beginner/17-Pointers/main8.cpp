#include <iostream>

int main() {

    int a = 10;

    int *ptr = &a;

    int **pptr = &ptr;

    std::cout << ptr << std::endl;
    std::cout << pptr << std::endl;

    return 0;
}