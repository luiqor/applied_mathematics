import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Функція для обчислення координат кардіоїди в полярних координатах
def cardioid(theta):
    r = 1 + np.cos(theta)
    return r

# Функція для ініціалізації анімації
def init():
    line.set_data([], [])
    ball.set_data([], [])
    
    # Кутові значення для кардіоїди
    theta = np.linspace(0, 2 * np.pi, 100)
    r_cardioid = cardioid(theta)
    line.set_data(theta, r_cardioid)

    return line, ball

# Функція для оновлення кадру анімації
def update(frame):
    # Кутове значення для миготливої кульки
    ball_theta = frame * 0.1
    ball_r = cardioid(ball_theta)

    # Змінюємо прозорість кульки лише один раз протягом кожного періоду анімації
    alpha = 1.0 if frame % 2 == 0 else 0.0
    ball.set_data(ball_theta, ball_r)
    ball.set_alpha(alpha)

    return line, ball

# Створення пустого полярного полотна
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Ініціалізація лінії для кардіоїди та кульки
line, = plt.polar([], [])
ball, = ax.plot([], [], 'ro')
ax.set_rmax(2.5)  
ax.set_rmin(0) 
# Створення анімації
animation = FuncAnimation(fig, update, frames=63, init_func=init, blit=True, interval=20)

# Відображення анімації
plt.show()
