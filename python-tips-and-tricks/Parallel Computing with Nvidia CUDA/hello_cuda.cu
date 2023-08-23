// nvcc hello_cuda.cu -o hello_cuda

#include <stdio.h>

__global__ void hello_cuda() {
    printf("hello cuda\n");
    printf("Block Index x: %d, block index y: %d, thread index x: %d, thread index y: %d\n", blockIdx.x, blockIdx.y, threadIdx.x, threadIdx.y)
}

int main(int argc, char **argv) {
    hello_cuda<<<2,2>>>();
    cudaDeviceSynchronize();

    return 0;
}
