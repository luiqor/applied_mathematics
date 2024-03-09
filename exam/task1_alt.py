import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# Створення фігури та вісей
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)  # обмеження по координатам для коректного відображення
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')  # щоб було однаково x до y

# Створення кола як matplotlib.patches
circle = Circle((0, 0), 0.3, fc='magenta', animated=True)
ax.add_patch(circle)
background_circle = Circle((0, 0), 0.8, fc='black')
ax.add_patch(background_circle)

# Функція оновлення кадру анімації
def update(frame):
    # кут повороту для кожного кадру
    angle = (frame / 100) * 360  # 100 як кількість кадрів за які шлях. 360 це повний шлях кола
    angle_rad = np.radians(angle)

    # тригонометричні функції для визначення координат кола по якому рухається міні-коло
    x = 0.4 * np.cos(angle_rad)
    y = 0.4 * np.sin(angle_rad)

    # для зміни
    circle.set_center((x, y))
    return circle,

# Створення об'єкту анімації, де 100 кадрів
ani = FuncAnimation(fig, update, frames=np.arange(0, 100),  blit=True, interval=20)

# Показ анімації
plt.show()
ani.save('Anim.gif', writer='pillow', fps=40)
