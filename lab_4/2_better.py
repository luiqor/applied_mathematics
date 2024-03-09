import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


x = np.linspace(-1.3, 1.3, 100)
y = np.linspace(-1.3, 1.3, 100)
X, Y = np.meshgrid(x, y)


Z1 = X**2 + Y**2
Z2 = X


A = 0.5
w = 0.1  # Increased frequency for surf1
frames = 200  # Total number of frames
angle_increment = 360 / frames  # Angle increment for each frame
cycles = 2

def init():
    ax.plot_surface(X, Y, Z1, color='g')
    ax.plot_surface(X, Y, Z2, color='b')
    return

def animate(i):
    limit = 3
    Z1_shift = Z1 + A * np.sin(w * i)

    angle = i * angle_increment
    Z2_rotated = Z2 * np.cos(np.radians(angle)) - Z2 * np.sin(np.radians(angle))

    ax.cla()
    ax.quiver(0, -1.8, 0, 0, 1.8*2, 0, arrow_length_ratio=0.3, colors='magenta')
    ax.quiver(-1.8, 0, 0, 1.8*2, 0, 0, arrow_length_ratio=0.3, colors='magenta')
    ax.quiver(0, 0, -1, 0, 0, 4+1, arrow_length_ratio=0.3, colors='magenta', capstyle='round')
    surf1 = ax.plot_surface(X, Y, Z1_shift, color='g')
    surf2 = ax.plot_surface(X, Y, Z2_rotated, color='b')

    ax.set_xlim([-limit, limit])
    ax.set_ylim([-limit, limit])
    ax.set_zlim([-limit, limit])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Перетин еліптичного параболоїда та площини')
    ax.view_init(elev=10, azim=i*4)
    return surf1, surf2

ani = FuncAnimation(fig, animate, init_func=init, frames=200, blit=False)
plt.show()

