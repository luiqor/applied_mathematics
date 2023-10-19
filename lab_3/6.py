import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-1.3, 1.3, 20)
y = np.linspace(-1.3, 1.3, 20)
X, Y = np.meshgrid(x, y)
Z1 = X**2 + Y**2
Z2 = X

fig = plt.figure()

# Місця розташування кожного графіка
left1, bottom1, width1, height1 = 0.1, 0.55, 0.4, 0.4  
left2, bottom2, width2, height2 = 0.55, 0.55, 0.4, 0.4  
left3, bottom3, width3, height3 = 0.3, 0.1, 0.4, 0.4  

# Перший графік
ax1 = fig.add_axes([left1, bottom1, width1, height1], projection='3d')
surf1 = ax1.plot_wireframe(X, Y, Z1, color='g')
surf2 = ax1.plot_wireframe(X, Y, Z2, color='b')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('Перетин еліптичного параболоїда та площини')
ax1.set_xlim3d([-1.8, 1.8])
ax1.set_ylim3d([-1.8, 1.8])
ax1.set_zlim3d([-1.4, 4])
ax1.quiver(0, -1.8, 0, 0, 1.8*2, 0, arrow_length_ratio=0.3, colors='magenta')
ax1.quiver(-1.8, 0, 0, 1.8*2, 0, 0, arrow_length_ratio=0.3, colors='magenta')
ax1.quiver(0, 0, -1, 0, 0, 4+1, arrow_length_ratio=0.3, colors='magenta', capstyle='round')

# Другий (Завдання 4 3 варіанту )
ax2 = fig.add_axes([left2, bottom2, width2, height2], projection='3d')
X = np.linspace(-10, 10, 20)
Y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(X, Y)
Z = (X**2 + 2*Y**2 - 4*X + 4*Y + 6) / 4
ax2.scatter(X, Y, Z, c=X, marker='.')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title('Розсіяний графік поверхні №4.1.2')

# Add the third subplot with a polar plot
ax3 = fig.add_axes([left3, bottom3, width3, height3], projection='polar')
fi = np.linspace(-np.pi, np.pi, 5000)
r = np.abs(3 * np.sin(2 * fi))
ax3.plot(fi, r, color='purple')
ax3.fill(fi, r, color='yellow')
ax3.set_title('Полярний графік')
plt.tight_layout()

plt.show()