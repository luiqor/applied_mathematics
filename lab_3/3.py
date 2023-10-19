import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Скоординатну сітку
x = np.linspace(-1.3, 1.3, 100)
y = np.linspace(-1.3, 1.3, 100)
X, Y = np.meshgrid(x, y)

Z1 = X**2 + Y**2
Z2 = X

fig = plt.figure()
ax=Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')

surf1 = ax.plot_surface(X, Y, Z1, color='g')
surf2 = ax.plot_surface(X, Y, Z2, color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Перетин еліптичного параболоїда та площини')

# обмеження осей
ax.set_xlim3d([-1.8,1.8])
ax.set_ylim3d([-1.8,1.8])
ax.set_zlim3d([-1.4,4])

# стрілки по центру
ax.quiver(0, -1.8, 0, 0, 1.8*2, 0, arrow_length_ratio=0.3, colors='magenta')
ax.quiver(-1.8, 0, 0, 1.8*2, 0, 0, arrow_length_ratio=0.3, colors='magenta')
ax.quiver(0, 0, -1, 0, 0, 4+1, arrow_length_ratio=0.3, colors='magenta', capstyle = 'round')

plt.show()

#підтянти ці всі графіки, пофіксити всякі приколи і тп, зробити середню лінію як на

#GOOD