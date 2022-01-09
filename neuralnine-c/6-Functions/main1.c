#include <stdio.h>
#include <stdbool.h>

bool is_even(int n);

int main() {
    int a;
    scanf("%d", &a);

    if (is_even(a)) {
        printf("a is even!\n");
    }
    return 0;
}

bool is_even(int n) {
    return n % 2 == 0;
}