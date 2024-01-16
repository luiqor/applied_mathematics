import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Polygon
from matplotlib.animation import FuncAnimation

# Create figure and axes
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Create an ellipse
ellipse = Ellipse((0, 0), 0.2, 0.15, fc='black', animated=True)
ax.add_patch(ellipse)

# Create a diamond
diamond = Polygon([(0, 1), (1, 0), (0, -1), (-1, 0)], fc='red', alpha=0.3)
ax.add_patch(diamond)

# Animation initialization function
def init():
    return ellipse,

# Animation update function
def update(frame):
    if frame <= 50:
        x_shift = -(frame / 50) *0.8 + 0.4
        y_shift = -(frame / 50) *0.8 + 0.4
    else:
        x_shift = -((100 - frame) / 50) *0.8 + 0.4
        y_shift = -((100 - frame) / 50) *0.8 + 0.4

    # Set the center of the ellipse using the shift logic
    ellipse.set_center((x_shift, y_shift))


    return ellipse,

# Create animation object
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=20)

# Show the animation
plt.show()
ani.save('pr9.gif', writer='pillow', fps=40)