import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.patches import Wedge

fig, ax = plt.subplots()
fig.set_facecolor('white')
my_patches = []

# Кола
circle1 = patches.Ellipse((5, 4), 5, 3, edgecolor='black', facecolor='green')
my_patches.append(circle1)

circle2 = patches.Ellipse((5, 7.5), 5, 3, edgecolor='black', facecolor='yellow')
my_patches.append(circle2)

circle3 = patches.Ellipse((5, 11), 5, 3, edgecolor='black', facecolor='red')
my_patches.append(circle3)

# Додавання всіх фігур до графічної області
for patch in my_patches:
    ax.add_patch(patch)
  
iterations = 10
# Функція для анімації
def anim(frame):
    # Змінюємо колір у відповідності до поточної ітерації
    if frame % 16 == 0:
        circle1.set_facecolor('green')
        circle2.set_facecolor('black')
        circle3.set_facecolor('black')
 
    elif frame % 16 == 4:
        circle1.set_facecolor('black')
        circle2.set_facecolor('black')
        circle3.set_facecolor('red')      
     
    elif frame % 16 == 8:
        circle1.set_facecolor('green')
        circle2.set_facecolor('black')
        circle3.set_facecolor('black')
    
    elif frame % 16 == 11:
        circle1.set_facecolor('black')
        circle2.set_facecolor('black')
        circle3.set_facecolor('black')
        
    elif frame % 16 == 12:
        circle1.set_facecolor('black')
        circle2.set_facecolor('yellow')
        circle3.set_facecolor('black')
    
    elif frame % 16 == 13:
        circle1.set_facecolor('black')
        circle2.set_facecolor('black')
        circle3.set_facecolor('black')
        
    elif frame % 16 == 14:
        circle1.set_facecolor('black')
        circle2.set_facecolor('yellow')
        circle3.set_facecolor('black')
    
    elif frame % 16 == 15:
        circle1.set_facecolor('black')
        circle2.set_facecolor('black')
        circle3.set_facecolor('black')

# Створення анімації
ani = FuncAnimation(fig, anim, frames=iterations * 16, interval=200, repeat=False)
  
# Встановлення відповідних меж та сітки
ax.set_xlim(0, 10)
ax.set_ylim(0, 15)
ax.set_aspect('equal')
ax.grid(False)

plt.show()