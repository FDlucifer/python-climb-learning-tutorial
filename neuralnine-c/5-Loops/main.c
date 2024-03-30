#include <stdio.h>

int main() {
    int counter = 0;
    int limit;

    scanf("%d", &limit);

    // while (counter < limit) {
    //     printf("%d\n", ++counter);
    // }

    do {
        printf("%d\n", ++counter);
    } while (counter < limit);
    

    return 0;
}