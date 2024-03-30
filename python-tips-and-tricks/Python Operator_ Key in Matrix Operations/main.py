import numpy as np

A = np.matrix([[1,2],[3,4]])

B = np.matrix([[0,5],[10,15]])

C = np.matrix([[None,None],[None,None]])

C[0,0] = A[0,0] * B[0,0] + A[0,1] * B[1,0]

C[0,1] = A[0,0] * B[0,1] + A[0,1] * B[1,1]

C[1,0] = A[1,0] * B[0,0] + A[1,1] * B[1,0]

C[1,1] = A[1,0] * B[0,1] + A[1,1] * B[1,1]

print(C)
print(np.matmul(A,B))
print(A@B)

