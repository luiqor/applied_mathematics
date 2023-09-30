import numpy as np
A = np.array([[ 1, 1,-2, 1, 3],
              [-1, 2, 1,-1,-2],
              [ 3, 0,  2, 1,-1],
              [ 3, 3, 1, 1,-1]])
print(np.linalg.matrix_rank(A))