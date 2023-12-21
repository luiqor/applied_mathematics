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

# Animation initialization function
def init():
    diamond = Polygon([(0, 1), (1, 0), (0, -1), (-1, 0)], fc='red', alpha=0.3)
    ax.add_patch(diamond)
    return ellipse,

# Animation update function
def update(frame):
    # Define the rotation angle for each frame
    angle = (frame / 100) * 360
    angle_rad = np.radians(angle)

    # Use trigonometric functions to determine the ellipse coordinates
    x = 0.5 * np.cos(angle_rad)
    y = 0.3 * np.sin(angle_rad)  # Adjust the y-radius to make it an ellipse

    # Set the center and angles of the ellipse
    ellipse.set_center((x, y))
    ellipse.set_angle(angle)
    return ellipse,

# Create animation object
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=20)

# Show the animation
plt.show()
