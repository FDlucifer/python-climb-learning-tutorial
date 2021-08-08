#include <iostream>
#define PI (3.14159)
#define ARR_SIZE (128)

#define square(a) a * a

int main() {
    int i = 5;
    std::cout << PI << std::endl;
    std::cout << square(i++) << std::endl;
    std::cout << i << std::endl;
    return 0;
}