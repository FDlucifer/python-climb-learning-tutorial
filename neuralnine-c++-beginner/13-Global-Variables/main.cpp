#include <iostream>
#include "includes/myfile.h"
//g++ main.cpp -o main.exe includes/myfile.cpp

int x = 100;
extern int test;

int myfunction() {
    std::cout << add_to_x(10) << std::endl;
    std::cout << test << std::endl;
    return 0;
}

int main() {
    myfunction();
    return 0;
}