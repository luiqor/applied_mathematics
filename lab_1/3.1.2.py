import numpy as np
# запишемо систему у матричній формі AX=B —> X = A^-1 * B
#основна матриця системи A
A = np.array([[ 2, 1, 1],
              [ 1, 2, 1],
              [ 1, 1, 2]])
#матриця правої частини B
B = np.array([[ 2],
              [ 3],
              [-1]])

#визначник А
deltaA = np.linalg.det(A)
print("Переконаємось що визначник не = 0, визначник матриці A:  ", deltaA)

# a) - матричним методом
#обернена матриця -
A1 =  np.linalg.inv(A)

X = np.dot(A1, B)
print("Матричний метод, матриця невідомих X:")
print(X)

# б) - за формулою Крамера
#по черзі b1,b2,b3 замість стовпців
C = np.array([[ 2, 1, 1],
              [ 3, 2, 1],
              [-1, 1, 2]])
deltaX1 = np.linalg.det(C)

D = np.array([[ 2, 2, 1],
              [ 1, 3, 1],
              [ 1,-1, 2]])
deltaX2 = np.linalg.det(D)

F = np.array([[ 2, 1, 2],
              [ 1, 2, 3],
              [ 1, 1,-1]])
deltaX3 = np.linalg.det(F)

X1 = round(deltaX1/deltaA)
X2 = round(deltaX2/deltaA)
X3 = round(deltaX3/deltaA)
print("За формулою Крамера X1: ", X1, ", X2: ", X2, ", X3: ", X3)

X_kramer = np.array([[X1],[X2],[X3]])
print("Крамер, матриця невідомих X:\n", X_kramer)

print("Перевірка, де B:")
print(np.dot(A,X))