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

number_bars = 6
xs = np.arange(number_bars)
ys = np.random.rand(number_bars)

# Колір
colors1 = plt.get_cmap('viridis')(ys)
colors2 = plt.get_cmap('hsv')(ys)
colors3 = plt.get_cmap('plasma')(ys)

ax.bar(xs, ys, zs=0, zdir='x', color=colors1)
ax.bar(xs, ys, zs=1, zdir='x', color=colors2)

zs3 = np.linspace(0.05, 1, number_bars)
ax.bar(xs, ys, zs3, zdir='y', color=colors3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Діаграми')

plt.show()