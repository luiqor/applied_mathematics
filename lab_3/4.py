import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def xc(Abs, u, v):
    return Abs(u) - Abs(u - 1) - Abs(u - 2) + Abs(u - 3)

def yc(Abs, u, v):
    return 1 + Abs(v) - Abs(v - 1)

def zc(Abs, u, v):
    return 1 - Abs(Abs(u - 1) - Abs(u - 2) - Abs(u - 3) + Abs(u - 4) +
                   Abs(v - 1) - Abs(v - 2) + Abs(v) - Abs(v + 1)) / 2 + \
           Abs(2 + Abs(u - 1) - Abs(u - 2) - Abs(u - 3) +
               Abs(u - 4) + Abs(v - 1) - Abs(v - 2) + Abs(v) - Abs(v + 1)) / 2

# зображення куба
u = np.linspace(0, 4, 41)
v = np.linspace(-1, 2, 31)
U, V = np.meshgrid(u, v)
X = xc(np.abs, U, V)
Y = yc(np.abs, U, V)
Z = zc(np.abs, U, V)

fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, color='0.75', alpha=0.85)
ax.axis('image')

# зображення синусоїд на всіх гранях куба
for i in range(len(u)-1):
    x = np.linspace(u[i], u[i+1], 100)
    y = np.sin(8 * np.pi * x) / 2 + 1
    zer = np.zeros(np.size(x))
    ax.plot(x, y, 2, linewidth=2, color='r')

plt.show()
