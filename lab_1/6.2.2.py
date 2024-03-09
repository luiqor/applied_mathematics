import numpy as np
A = np.array([-3,5,4])
B = np.array([0,0,8])
C = np.array([-1,3,2])
D = np.array([2,6,1])

#vAB - вектор AB і т.д.
vAB= B - A
vAC= C - A
vAD= D - A
#спрощена

# векторний добуток np.cross()
ABxAC = np.cross(vAB, vAC)
# np.linalg.norm() - знаходимо довжину(модуль) вектора
S_ABC = np.linalg.norm(ABxAC) / 2

print("Площа грані ABC")
print(round(S_ABC, 2))


ABCD = np.array([vAB, vAC, vAD])
#мішайни добуток = визначнику, тож
detABCD = round(np.linalg.det(ABCD))
#np.abs - це модуль
V_ABCD = np.abs(detABCD / 6 )
print("Об'єм піраміди ABCD")
print(round(V_ABCD, 2))