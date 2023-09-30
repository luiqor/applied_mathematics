import numpy as np
import math
# а)
fi = 2 * math.pi/3
a = 3
b = 4
A = 6 * a**2 + a * b * math.cos(fi) - 10 * b**2
print(A)

# б)
B = math.sqrt( a**2 - 6 *a *b * math.cos(fi) + 9 * b**2 )
Br= round(B, 2)
print(Br)