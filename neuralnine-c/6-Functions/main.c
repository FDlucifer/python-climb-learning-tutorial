#include <stdio.h>

int add(int a, int b);
void say_hello(void);

int main() {
    int c = add(10, 20);
    printf("%d\n", c);
    printf("%d\n", add(30, 40));
    say_hello();
    return 0;
}

int add(int a, int b) {
    return a + b;
}

void say_hello() {
    for (int i = 0; i < 5; i++) {
        printf("hello world!\n");
    }
}