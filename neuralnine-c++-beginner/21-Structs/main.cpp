#include <iostream>

struct mystruct {
    int i;
    std::string s;
    bool b;

    void test() {
        std::cout << "this is a fuck" << std::endl;
    }
};

int main() {

    struct mystruct m1;
    m1.i = 20;
    m1.s = "fuck";
    m1.b = true;

    struct mystruct m2;

    std::cout << m1.i << std::endl;
    std::cout << m1.s << std::endl;
    std::cout << m1.b << std::endl;

    m1.test();

    std::cout << m2.i << std::endl;
    std::cout << m2.s << std::endl;
    std::cout << m2.b << std::endl;

    m2.test();
    return 0;
}