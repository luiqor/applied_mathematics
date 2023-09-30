import numpy as np
#A * X = B
A = np.array([[4,3],
              [1,1]])
B = np.array([[2,8],
              [1,1],
              [0,-1]])
#матриці є неузгодженими, тож X * A * A^-1 = B * A^-1,   X * E = B * A^-1,    X=B*A^-1
#знаходжу обернену матрицю A
A1 =  np.linalg.inv(A)

X = np.linalg.solve(A,B) 
print(X)


#np.linalg.solve(A,B) 