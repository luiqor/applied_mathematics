import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle, Circle

fig = plt.figure(facecolor='white')
ax = plt.axes(xlim=(0, 8), ylim=(-1, 1))
line, = ax.plot([], [], lw=3)  # line = об'єкт кривої
ax.grid(True)


def redraw(i):
    x = np.linspace(0, 8, 200)
    y = np.sin(i * x / 10) / (1 + x ** 2)
    line.set_data(x, y)


# результат обов'язково привласнювати змінної
anim = animation.FuncAnimation(fig, redraw, frames=100, interval=50)


def initpict():
    rect = Rectangle((1, -0.5), 4, 1, facecolor='cyan', fill=True)
    ax.add_patch(rect)  # додавання прямокутника на графічну область
    circle = Circle((2, 0), 0.5, color='r')
    ax.add_artist(circle)  # додавання кола на графічну область


ax.set_aspect('equal')
initpict()  # Call initpict to initialize the patches before the animation

# Use initpict function in init_func parameter
anim = animation.FuncAnimation(fig, redraw, init_func=initpict, frames=100, interval=50)

plt.show()
