import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


x = np.linspace(-1.3, 1.3, 20)
y = np.linspace(-1.3, 1.3, 20)
X, Y = np.meshgrid(x, y)


Z1 = X**2 + Y**2
Z2 = X

# 3D графік вікна номер 1  Помістити в першу область каркасний графік поверхні (Ваш варіант з альбому поверхонь) +
fig = plt.figure()
ax=Axes3D(fig)
ax = fig.add_subplot(2,2, 1, projection='3d')

surf1 = ax.plot_wireframe(X, Y, Z1, color='g')

surf2 = ax.plot_wireframe(X, Y, Z2, color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Перетин еліптичного параболоїда та площини')

ax.set_xlim3d([-1.8,1.8])
ax.set_ylim3d([-1.8,1.8])
ax.set_zlim3d([-1.4,4])

ax.quiver(0, -1.8, 0, 0, 1.8*2, 0, arrow_length_ratio=0.3, colors='magenta')
ax.quiver(-1.8, 0, 0, 1.8*2, 0, 0, arrow_length_ratio=0.3, colors='magenta')
ax.quiver(0, 0, -1, 0, 0, 4+1, arrow_length_ratio=0.3, colors='magenta', capstyle = 'round')


# 3D графік вікна номер 2 Помістити в другу область розсіяний графік поверхні (Ваш варіант з Лабораторної 3 Завд.4) +
X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = (X**2 + 2*Y**2 - 4*X + 4*Y + 6) / 4

ax = fig.add_subplot(2, 2, 2, projection='3d')
ax.scatter(X,Y,Z, c='b', marker='.')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Z = (X**2 + 2*Y**2 - 4*X + 4*Y + 6) / 4')


# # 3D графік вікна номер 3 В третій області накласти контурний графік в полярних координатах на залитий контурний графік (Ваш варіант файл Полярні координати 2.pdf).
# fi = np.linspace(0, 2 * np.pi, 1000)
# r = 3 * np.sin(2 * fi)
# x = r * np.cos(fi)
# y = r * np.sin(fi)

# ax = fig.add_subplot(2, 2, 3, projection='3d')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('r = 3 * sin(2 * fi)')

# # ax.plot_trisurf(x, y, r, cmap='viridis')
# verts = [list(zip(x, y, r))]
# ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan'))

# ax.plot(x, y, r, color='orange',linewidth=4)

# 3D графік вікна номер 3 В третій області накласти контурний графік в полярних координатах на залитий контурний графік (Ваш варіант файл Полярні координати 2.pdf).
# plt.figure(figsize=(6, 6))


fi = np.linspace(-np.pi, np.pi, 5000)
r = 3 * np.sin(2 * fi)
ax = fig.add_subplot(2, 2, 3)

plt.polar(fi, r, "r", label='ro = 3 / (1+ 2 * np.cos(fi))')
#Пофіксити 3 

plt.show()