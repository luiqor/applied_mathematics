import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax=Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(X, Y)
Z = (X**2 + 2*Y**2 - 4*X + 4*Y + 6) / 4
ax.plot_surface(X, Y, Z, cmap='plasma')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Графік поверхні №4.1.2')

origin = [0], [0], [0]
ax.quiver(*origin, 1, 0, 0, color='g', length=10)
ax.quiver(*origin, 0, 1, 0, color='g', length=10)
ax.quiver(*origin, 0, 0, 1, color='g', length=80, arrow_length_ratio=0.1)

plt.show()