#include <iostream>

int main() {
    int arr[100];

    std::cout << &arr << std::endl;
    std::cout << &arr[0] << std::endl;
    std::cout << &arr[1] << std::endl;
    std::cout << &arr[2] << std::endl;
    std::cout << &arr[3] << std::endl;

    int *ptr = arr;
    std::cout << ptr << std::endl;

    return 0;
}