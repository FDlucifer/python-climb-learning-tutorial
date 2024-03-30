#include <iostream>

//int add(int, int);
int add(int, int=50, int=90);
std::string add(std::string, std::string);
int f1(void);
int f2(void);
bool isGreaterThan(int, int);
void myfunction(void);

int main() {

    std::cout << add(10) << std::endl;
    std::cout << add(10,20) << std::endl;
    std::cout << add(10,20,30) << std::endl;
    std::cout << isGreaterThan(10,5) << std::endl;
    myfunction();

    std::cout << add("fuck", " world!") << std::endl;

    return 0;
}

/*int add(int x, int y) {
    return x + y;
}*/

int add(int x, int y, int z) {
    std::cout << "using three parameters!" << std::endl;
    return x + y + z;
}

std::string add(std::string s1, std::string s2) {
    return s1 + s2;
}

int f1(void) {
    // f2()
    return 0;
}

int f2(void) {
    // f1()
    return 0;
}

bool isGreaterThan(int x, int y) {
    return x > y;
}

void myfunction(void) {
    std::cout << "fuck world!" << std::endl;
}