#include <iostream>
#include <limits.h>

int main() {
    // numerical data types
    std::cout << "short (short): " << sizeof(short) << std::endl;
    std::cout << "Integer (int): " << sizeof(int) << std::endl;
    std::cout << "Long (long): " << sizeof(long) << std::endl;
    std::cout << "Long (long): " << sizeof(long long) << std::endl;

    std::cout << "Float: " << sizeof(float) << std::endl; //7 digits
    std::cout << "Double: " << sizeof(double) << std::endl; // 15 digits

    std::cout << INT_MAX << std::endl;
    std::cout << INT_MIN << std::endl;
    std::cout << UINT_MAX << std::endl;
    std::cout << SHRT_MAX << std::endl;
    std::cout << LONG_LONG_MAX << std::endl;

    unsigned int s = 65535;
    std::cout << s << std::endl;
    // Textual Data Types

    char c = 'a';
    std::cout << sizeof(char) << std::endl;
    std::cout << c << std::endl;

    std::string g = "fuck world!";
    std::cout << g << std::endl;
    std::cout << sizeof(std::string) << std::endl;

    // Boolean

    bool b = true;
    std::cout << b << std::endl;
    std::cout << sizeof(bool) << std::endl;

    return 0;
}