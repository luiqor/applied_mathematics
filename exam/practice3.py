import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

x = sp.Symbol('x') 
integral = sp.integrate(((3*x+13)/(x**2 + 2 *x +5)), x)
print("інтеграл:" ) 
sp.pprint(integral)

# Перевторення символьного виразу на функцію Python для числового обчислення
integral_func = sp.lambdify(x, integral, 'numpy')

x_values = np.linspace(-30, 50, 100) 

# Обчислення відповідних значень y з заданими x_values
y_values = integral_func(x_values)

# Для побудови графіка
fig, ax = plt.subplots()
ax.set_xlim(-20 , 20)
ax.set_ylim(-20 , 20) 

ax.plot(x_values, y_values, color = 'purple', alpha=0.5, linestyle='--', label='Оригінальний графік похідної')
ax.set_title('Анімація графіка')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()
ax.grid()


line, = ax.plot([], [], lw=2, color='purple', label='Анімація')


def init():
    line.set_data([], [])
    return line,


def animate(i):
    if i <= 50:
        x_shift = -(i / 50) * 40 + 20
        y_shift = -(i / 50) * 40 + 20
    else:
        x_shift = -((100 - i) / 50) * 40 + 20
        y_shift = -((100 - i) / 50) * 40 + 20

    line.set_data(x_values + x_shift, y_values + y_shift)
    return line,


ani = FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True, repeat=True)

plt.legend()
plt.show()