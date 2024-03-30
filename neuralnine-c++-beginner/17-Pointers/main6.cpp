#include <iostream>

int main() {

    int a = 20;
    void *vp = &a;

    std::cout << vp << std::endl;

    return 0;
}