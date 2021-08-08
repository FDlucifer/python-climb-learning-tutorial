#include <iostream>

int main() {
    int a = 10;

    int *ptr = &a;

    // do sth with ptr

    ptr = 0;
    ptr = NULL; // C

    ptr = nullptr;
    if (ptr == 0) {
        std::cout << "message" << std::endl;
    }

    return 0;
}