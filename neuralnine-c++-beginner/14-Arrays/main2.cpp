#include <iostream>

int main() {

    int a;
    std::cin >> a;

    int myarray[a] = {10, 80, 20};

    for (int i = 0; i < a + 10; i++) {
        std::cout << myarray[i] << std::endl;
    }

    return 0;
}