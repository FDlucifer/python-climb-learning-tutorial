#include <stdio.h>

int main() {
    int a = 10;
    int *mypointer = &a;

    printf("%p\n", mypointer);
    printf("%d\n", *mypointer);

    *mypointer = 20;
    printf("%d\n", a);

    printf("%ld\n", sizeof(mypointer));
    printf("%p\n", mypointer);
    printf("%p\n", &mypointer);

    int **pptr = &mypointer;
    printf("%p\n", pptr);
    printf("%p\n", *pptr);
    printf("%d\n", **pptr);

    return 0;
}