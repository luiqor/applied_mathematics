# Побудувати три просторові діаграми. (набір стовпчиків) в
# просторі. Кількість стовбчиків Варіант +4. Висоту стовбчиків задавати
# np.random. Усі діаграми будувати в одному вікні. Самі діаграми
# зробити різнокольровими.

# Перша і друга розташовані в площинах х = 0 і х = 1. Площині стовпчиків
# третьої діаграми змінюються від y = 0.05 до 1.

from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs1 = np.arange(6) # x координаты лівих нижніх кутів стовбцівys1 = np.random.rand(20) # масив 20 чисел з діапазону [0,1)
ys1 = np.random.rand(6) # масив 20 чисел з діапазону [0,1)
zs1=np.zeros(len(xs1)) # z координати стовбців
cs1 = ['c'] * len(xs1) # колір стовбців
ax.bar(xs1, ys1, zs1)

xs2 = np.arange(6)
ys2 = np.random.rand(6) # масив 20 чисел з діапазону [0,1)
zs2=np.ones(len(xs2)) # z координати стовбців
cs2 = ['g'] * len(xs2) # колір стовбців
ax.bar(xs2, ys2, zs2)

xs3 = np.arange(6)
ys3 = np.random.rand(6)
zs3 = np.linspace(0.05,1,6) # z z координати стовбців
cs3 = ['r'] * len(xs3) # колір стовбців
ax.bar(xs3, ys3, zs3)

plt.show()import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the number of columns and their properties
num_columns = 6
x_positions = [0, 1]
y_range = np.linspace(0.05, 1, num_columns)
colors = np.random.rand(num_columns, 3)  # Generate random colors for columns

# Create the first two diagrams at x = 0 and x = 1
for x in x_positions:
    for i in range(num_columns):
        ax.bar(x, 1, y_range[i], zdir='y', color=colors[i])

# Create the third diagram with varying y-positions
for i in range(num_columns):
    ax.bar(2, 1, y_range[i], zdir='y', color=colors[i])

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
