import sympy as sp
import math
# модуль а=3, модуль b=4 
a = sp.Symbol('a')
b = sp.Symbol('b')
fi= 2 * math.pi/3
fiCos = round(math.cos(fi), 1)
print("косінус fi: ", fiCos)

# XA - а) 
XA = sp.expand((2*a + 5*b)*(3*a-2*b))
print("а): ",XA)
XA=  XA.evalf(subs={a**2:9,b**2:16,a*b:3*4*fiCos})
#subs підставляє і обчислює
#X2.evalf до A звертається до мин. приклада
print("відповідь а): ",round(XA))

# XB - б) 
XB= sp.expand(sp.sqrt((a-3*b)**2))
print("б): ",XB)
XB=  XB.evalf(subs={a**2:9,b**2:16,a*b:3*4*fiCos})
print("відповідь б): ",round((XB), 2))