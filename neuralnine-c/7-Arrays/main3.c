#include <stdio.h>

void print_array(int array[], int size);

int main() {
    int mymultiarray[2][3] = {
        {2,3,4},
        {1,5,7}
    };

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%d\n", mymultiarray[i][j]);
        }
    }

    char myname[10] = "lUc1f3r11";
    char myother[10] = "HEELLOOO";

    int mynumbers[] = {1,2,3,4,5,6,7,8,9,0};

    printf("%s\n", myname);
    printf("%ld\n", sizeof(mynumbers) / sizeof(0));
    printf("%ld\n", sizeof(myname));

    return 0;
}

void print_array(int array[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d\n", array[i]);
    }
}