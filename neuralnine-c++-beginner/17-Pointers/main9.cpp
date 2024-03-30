#include <iostream>

void function1() {
    std::cout << "i am function one!" << std::endl;
}

void function2() {
    std::cout << "i am function two!" << std::endl;
}

int main() {
    void (*myfunc)();
    myfunc = function1;
    myfunc();
    myfunc = function2;
    myfunc();

    return 0;
}