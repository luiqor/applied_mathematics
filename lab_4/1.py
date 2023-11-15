import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

 
t = np.linspace(-np.pi, np.pi, 1000)
x = np.log(np.tan(t))  
y = 1 / (np.cos(t)**2)


fig, ax = plt.subplots()
ax.set(xlim=(-10, 9.3), ylim=(-2, 15)) 
ax.grid()
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)


line, = ax.plot([], [], color='blue')
colors = ['blue', 'red', 'green', 'purple']
ax.set(xlabel='x', ylabel='y', title='Параметрично задана крива') 


def init():
    line.set_data([], [])
    return line,


def animate(i):
    
    x_shift = (i / 100) * 18 - 10
    if x_shift > 8: 
        x_shift = 8 - (x_shift - 8) #8 "-" задає зворотній напрямок, а (зсув- 8) визначає де зараз крива
    #% колір буде вибиратися з початку списку, коли індекс перевищує останній доступний індекс у списку   
    line.set_color(colors[i // 20 % len(colors)]) 
    # Update plot
    line.set_data(x + x_shift, y)

    return line,


ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=25, blit=True)

plt.show()