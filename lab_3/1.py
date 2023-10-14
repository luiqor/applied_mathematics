import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.patches import Circle, Wedge, Polygon, Rectangle, Arrow
from matplotlib.collections import PatchCollection

fig, ax = plt.subplots(figsize=(8, 8))

# Півколо
half_circle = Wedge(center= (12, 12), r=3, theta1=0, theta2=180, color='blue')
ax.add_patch(half_circle)

# Стрілка
arrow = Arrow(6, 7, 4, 4, width=0.9, color='green')
ax.add_patch(arrow)

# Трикутник
polygon = Polygon([[9, 5], [11, 9], [13, 5]], closed=True, color='red')
ax.add_patch(polygon)

# Сектор
# wedge = Wedge((4, 14), 3, 0, 45, color='purple')
wedge = Wedge(center=(4, 14), r=3, theta1=0, theta2=45, color='purple')
ax.add_patch(wedge)

# Ромб
vertices = np.array([[5, 3], [7, 5], [5, 7], [3, 5]])
rhombus = Polygon(vertices, closed=True, color='orange')
ax.add_patch(rhombus)

# Прямокутник
rectangle = Rectangle((10, 1), 4, 2, color='magenta')
ax.add_patch(rectangle)

ax.set_xlim(0, 18)
ax.set_ylim(0, 18)
ax.set_aspect('equal')

plt.show()
#GOOD