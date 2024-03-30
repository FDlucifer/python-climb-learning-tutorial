#include <iostream>
#include <bits/stdc++.h>
#include <stdint.h>

typedef unsigned char byte;
typedef std::bitset<8> bytetype;

int main() {
    byte b = 70;
    byte b2 = 20;
    byte b3 = b + b2;

    std::cout << b << std::endl;
    std::cout << unsigned(b) << std::endl;
    std::cout << b + b2 << std::endl;
    std::cout << b3 << std::endl;
    std::cout << sizeof(b3) << std::endl;

    bytetype mb = 100;
    std::cout << mb << std::endl;
    std::cout << sizeof(mb) << std::endl;

    return 0;
}