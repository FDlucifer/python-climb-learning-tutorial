#include <stdio.h>

__global__ void matrix_vector_product(float *A, float *v1, float *v2, int matrix_size) {
    int row = blockIdx.x * blockDim.x + threadIdx.x;
    int col = blockIdx.y * blockDim.y + threadIdx.y;

    if (col == 0 && row < matrix_size) {
        float sum = 0.0f;
        for (int i = 0; i < matrix_size; i++) {
            sum += A[row * matrix_size + i] * v1[i];
        }
        v2[row] = sum;
    }
}

int main(int argc, char **argv) {
    float *A, *A_gpu;
    float *v1, *v1_gpu;
    float *v2, *v2_gpu;

    int matrix_size = 3;

    dim3 block_shape = dim3(32,32);

    dim3 grid_shape = dim3(max(1.0, ceil((float) matrix_size / (float) block_shape.x)),
                           max(1.0, ceil((float) matrix_size / (float) block_shape.y)));

    A = (float *) malloc(matrix_size * matrix_size * sizeof(float));
    v1 = (float *) malloc(matrix_size * sizeof(float));
    v2 = (float *) malloc(matrix_size * sizeof(float));

    for(int i = 0; i < matrix_size; i++) {
        for(int j = 0; j < matrix_size; j++) {
            A[i * matrix_size + j] = (float) i * matrix_size + j;
        }
    }

    for(int i = 0; i < matrix_size; i++) {
        v1[i] = (float) i;
    }

    cudaMalloc((void **) &A_gpu, matrix_size * matrix_size * sizeof(float));
    cudaMalloc((void **) &v1_gpu, matrix_size * sizeof(float));
    cudaMalloc((void **) &v2_gpu, matrix_size * sizeof(float));

    cudaMemcpy(A_gpu, A, matrix_size * matrix_size * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(v1_gpu, v1, matrix_size * sizeof(float), cudaMemcpyHostToDevice);

    matrix_vector_product<<<grid_shape, block_shape>>>(A_gpu, v1_gpu, v2_gpu, matrix_size);

    cudaMemcpy(v2, v2_gpu, matrix_size * sizeof(float), cudaMemcpyHostToDevice);

    for(int i = 0; i < matrix_size; i++) {
        printf("%.2f\n", v2[i]);
    }

    free(A);
    free(v1);
    free(v2);

    cudaFree(A_gpu);
    cudaFree(v1_gpu);
    cudaFree(v2_gpu);

    return 0;
}
