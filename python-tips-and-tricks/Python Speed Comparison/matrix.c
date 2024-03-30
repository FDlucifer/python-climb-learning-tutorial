#include <stdio.h>
#include <stdlib.h>

double A[500][500];
double B[500][500];
double C[500][500];

int main() {
    for (int i = 0; i < 500; i++) {
        for (int j = 0; j < 500; j++) {
            A[i][j] = (double) rand();
            B[i][j] = (double) rand();
            C[i][j] = 0;
        }
    }

    for (int i = 0; i < 500; i++) {
        for (int j = 0; j < 500; j++) {
            for (int k = 0; k < 500; k++) {
                C[i][j] += A[i][k] * B[k][j]
            }
        }
    }

    return 0;
}