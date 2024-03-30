#include <stdio.h>

int main() {
    int arr[100];
    printf("%p\n", arr);
    printf("%p\n", &arr[56]);

    int a = 10;
    int b = 20;
    int c = 30;
    int *ptr = &a;

    printf("%d\n", *ptr);
    ptr++;
    printf("%d\n", *ptr);
    printf("%d\n", *(++ptr));
    ptr--;
    printf("%d\n", *ptr);

    return 0;
}