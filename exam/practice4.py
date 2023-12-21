import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#вершини
vertices = np.array([
    [0, 0, 0],
    [2, 0, 0],
    [2, 2, 0],
    [0, 2, 0],
    [0, 0, 2],
    [2, 0, 2],
    [2, 2, 2],
    [0, 2, 2]
])

# грані куба
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[1], vertices[2], vertices[6], vertices[5]],
    [vertices[0], vertices[3], vertices[7], vertices[4]]
]

# вікно та "підвікно"
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Відобарзити грані куба
ax.add_collection3d(Poly3DCollection(faces, facecolors='purple', linewidth= 1, alpha=0.2, edgecolors='purple'))

# Set the aspect ratio to ensure the cube appears as a perfect cube
ax.set_box_aspect([2, 2, 2])

# Set the axis limits
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])

# зображення кіл на гранях куба
theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta) /1.5 +1 
y = np.sin(theta) /1.5 +1 
zer = np.zeros(np.size(theta))
ax.plot(x, y, zer+2, 'b', linewidth=2)
ax.plot(x, zer, y, 'r', linewidth=2)
ax.plot(x, zer+2, y, 'g', linewidth=2)
ax.plot(x, y, zer, 'purple', linewidth=2)
ax.plot(zer, x, y, 'orange', linewidth=2)
ax.plot(zer+2, x, y, 'cyan', linewidth=2)

ax.set_title('Куб з колами на гранях')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()


