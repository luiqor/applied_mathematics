import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from matplotlib.animation import FuncAnimation

# Creating figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-3, 8)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')

# Creating a circle
circle = Circle((0, 0), 1, fc='magenta', animated=True)
ax.add_patch(circle)

# Initialization function for animation
def init():
    rect = Rectangle((-1, -1.25), 7, 2.5, facecolor='cyan', fill=True)
    ax.add_patch(rect)  # додавання прямокутника на графічну область
    return circle,

# Update function for animation
def update(frame):
    if frame <= 50:
        x_shift = (frame / 50) * 4.6 + 0.2
    else:
        x_shift = ((100 - frame) / 50) * 4.6 + 0.2
    circle.set_center((x_shift, 0))
    return circle,

# Creating animation object
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=20, repeat=True)

# Showing the animation
plt.show()
