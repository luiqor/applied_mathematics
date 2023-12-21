import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
# Знайти похідну функції однієї змінної і зробити анімацію графіка отриманої функції (рух з лівої нижньої точки по діагоналі  до верхньої правої і назад): 
x = sp.symbols('x')
f = (sp.E**((2 * (x + 2)))) / (2 * (x + 2))

# Знаходження похідної
dydx = sp.diff(f, x)

#Похідна в спрощеній формі
dy_dx_simplified = sp.simplify(dydx)
print("Похідна в спрощеній формі")
sp.pprint(dy_dx_simplified) #красивий прінт для похідної в спрощеній формі 

#Перевторення символьних виразів на функції Python для числового обчислення
f_prime_func = sp.lambdify(x, dydx, 'numpy')

# Generate x values for the plot
x_values = np.linspace(-30, 20, 400)
y_prime_values = f_prime_func(x_values)


# Налаштування ддля графіка
fig, ax = plt.subplots()
ax.set_xlim(-12, 8)
ax.set_ylim(-12, 10) 
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.title('Анімація похідної')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

line, = ax.plot([], [], lw=2, color = 'purple', label='Анімація')

def init():
    line.set_data([], []) 
    return line,


def animate(i):
    if i <= 50: 
        # Анімація першої половини - (i/50) це відсоток від 0 до 1 шляху який пройшла крива. 
        #  * 20 це до якого значення на коориданатх має прибути крива. - 10 це початкоивй зсув графіка від оригінального положення
        x_shift = (i/50) * 20 - 10  
        y_shift = (i/50) * 20 - 10 

    else:
        # Анімація 2 половини
        x_shift = ((100-i)/50) * 20 - 10  
        y_shift = ((100-i)/50) * 20 - 10

    line.set_data(x_values + x_shift, y_prime_values + y_shift)
    return line,

ani = FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True, repeat=True) 


# на всякий випадок оригінальний(не похідна)
#f_func = sp.lambdify(x, f, 'numpy')
#y_values = f_func(x_values)
#plt.plot(x_values, y_values, label='Оригінальна')
plt.plot(x_values, y_prime_values, color = 'purple', alpha=0.5, linestyle='--', label='Оригінальний графік похідної')
plt.legend()
plt.show()