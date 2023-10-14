# Зробити графічний примітив. Додати в графічну область
# кольорову фігуру N багатокутник(N-варіант), контур зробити стрілочками та
# в середині зробити текст.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# # Стрілки по колу
N = 12
ang = np.linspace (0,2 * np.pi, N) 
x = np.cos (ang)
y = np.sin (ang)
fig = plt.figure (facecolor = 'white') 

ax = fig.add_subplot (111)
ax.fill(x, y, color='yellow')
arrows = [(x0, y0, dx, dy) for (x0, y0, dx, dy) in zip (x, y, np.diff (x), np.diff (y))] 
for x0, y0, dx , dy in arrows:
    ax.add_patch (patches.Arrow (x0, y0, dx, dy, width = 0.4)) 

ax.text(0, 0, '12-кутник', ha='center', va='center', fontsize=12, color='black')

plt.show()

#змінити щоб 12 кунтник був а не 11, див в умові для 3 кутника