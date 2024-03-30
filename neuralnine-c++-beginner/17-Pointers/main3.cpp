#include <iostream>

int main() {
    int arr[10];

    int *first_post = arr;

    for (int i = 0; i < 10; i++) {
        *(first_post + i) = i * 20;
    }

    for (int x : arr) {
        std::cout << x << std::endl;
    }

    return 0;
}