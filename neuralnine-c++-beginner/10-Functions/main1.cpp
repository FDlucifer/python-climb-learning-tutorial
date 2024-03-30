#include <iostream>

void myfunction() {
    static int x = 0;
    x++;
    std::cout << x << std::endl;
}

int main() {
    myfunction();
    myfunction();
    myfunction();
    myfunction();
    myfunction();
    myfunction();
    myfunction();
    myfunction();
    return 0;
}