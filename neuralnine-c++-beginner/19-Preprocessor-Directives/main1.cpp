#include <iostream>


int main() {
    #ifndef TRIGGER
    std::cout << "trigger is defined!" << std::endl;
    #endif
    
    return 0;
}