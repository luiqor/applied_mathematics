import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_cube():   
    phi = np.arange(1, 10, 2) * np.pi / 4
    Phi, Theta = np.meshgrid(phi, phi)

    x = np.cos(Phi) * np.sin(Theta)
    y = np.sin(Phi) * np.sin(Theta)
    z = np.cos(Theta) / np.sqrt(2)
    return x, y, z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y, z = get_cube()

x = x* 2 +1
y = y* 2 +1
z = z* 2 +1

ax.plot_surface(x, y, z, color='b', alpha=0.16)

# Set the aspect ratio to ensure the cube appears as a perfect cube
ax.set_box_aspect([2, 2, 2])

# Set the axis limits
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])

# зображення косинусоїд на гранях куба
x = np.linspace(0, 2, 100)
y = np.cos(4 * np.pi * x) / 2 + 1 # 4 забезпечує періодичність косинусоїди, /2 це щоб не на всю грань була косинусоїда (по її висоті), + 1 це щоб підняти їх від 0
zer = np.zeros(np.size(x))
ax.plot(x, y, zer+2, 'b', linewidth=2)
ax.plot(x, zer, y, 'r', linewidth=2)
ax.plot(x, zer+2, y, 'g', linewidth=2)
ax.plot(x, y, zer, 'purple', linewidth=2)
ax.plot(zer, x, y, 'orange', linewidth=2)
ax.plot(zer+2, x, y, 'cyan', linewidth=2)

ax.set_title('Куб з косинусоїдами на гранях')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
