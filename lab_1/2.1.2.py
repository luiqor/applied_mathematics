import numpy as np
A = np.array([[3,4,0],
              [1,2,3],
              [-3,1,-1]])
result = np.linalg.matrix_power(A,2) + 5 * A + 2 * np.eye(3)
                                                #* np.identity(3)
                                                #* np.ones(3) - не працює!!
print(result)
