import numpy as np
#основна матриця системи A, матриця правої частини B, матриця невідомих X
A= np.array([[ 1,-1, 2],
            [ 1,-1, 5],
            [ 1,-4, 8]])
B=np.array([2,8,2])
A1 = np.linalg.inv(A)
X=np.dot(B, A1)
print(np.round(X))

print("Перевірка\n", np.dot(X,A))

#можна розв без сумпай, можна значить з