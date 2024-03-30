#include <iostream>
#include <string.h>

int main() {
    std::string s = "fuck world";
    std::string s2("hello friends!");

    std::cout << s << " and " << s2 << std::endl;
    std::cout << s.length() << std::endl;

    std::cout << s[5] << std::endl;
    std::cout << s.at(5) << std::endl;

    if (s == s2) {
        std::cout << "same" << std::endl;
    } else {
        std::cout << "not same" << std::endl;
    }

    std::string combined = s + s2;
    std::cout << combined << std::endl;

    return 0;

}