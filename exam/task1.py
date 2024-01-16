import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# Створення фігури та вісей
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5) # обмеження по координатам для коректного відображення
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal') #щоб було однаково x до y

# Функція ініціалізації анімації
def init():
    global circle
    background_circle = Circle((0, 0), 0.8, fc='black') #коло на фон як matplotlib.patches 
    ax.add_patch(background_circle) #додати примітив у вікно

    # Створення кола як matplotlib.patches
    circle = Circle((0, 0), 0.3, fc='magenta', animated=True)
    ax.add_patch(circle)
    return circle, #відображенн япочтакового кола

# Функція оновлення кадру анімації
def update(frame):
    # кут повороту для кожного кадру
    angle = (frame / 100) * 360 #100 як кільк. кадрів за які шлях. 360 це шлях повне коло
    angle_rad = np.radians(angle)

    # тригонометричні функції для визначення координат кола по якому ходить міні коло
    x = 0.4 * np.cos(angle_rad)
    y = 0.4 * np.sin(angle_rad)
    
    # для зміни
    circle.set_center((x, y))
    return circle,


# Створення об'єкту анімації, де 100 кадрів
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), init_func=init, blit=True, interval=20)
ani.save('animated_circle3.gif', writer='pillow') 
# Показ анімації
plt.show()



