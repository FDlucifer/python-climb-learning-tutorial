#include <iostream>

void myfunction(int &x) {
    x++;
    std::cout << x << std::endl;
}

int main() {
    int a = 10;
    myfunction(a);
    std::cout << a << std::endl;

    // aliases

    int i1 = 10;
    int &integer1 = i1;

    std::cout << integer1 << std::endl;

    integer1 += 90;

    std::cout << i1 << std::endl;

    return 0;
}