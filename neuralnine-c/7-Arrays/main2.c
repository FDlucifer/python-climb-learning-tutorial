#include <stdio.h>

void print_array(int array[], int size);

int main() {
    int myarray[] = {1,2,3,4,5};
    print_array(myarray, 5);
    printf("%ld\n", sizeof(myarray) / sizeof(myarray[0]));

    return 0;
}

void print_array(int array[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d\n", array[i]);
    }
}