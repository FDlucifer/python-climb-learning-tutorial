#include <iostream>

int main() {

    char mychar = 'A';

    std::cout << (void *) &mychar << std::endl;

    return 0;
}