import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation


# Створення фігур та підготовка відображення
fig, ax = plt.subplots()


# Червоний еліпс
ellipse1 = patches.Ellipse((0.5, 0.8), width=0.4, height=0.2, facecolor='red', alpha=0)
ax.add_patch(ellipse1)

# Жовтий еліпс
ellipse2 = patches.Ellipse((0.5, 0.5), width=0.4, height=0.2, facecolor='yellow', alpha=0)
ax.add_patch(ellipse2)

# Зелений еліпс
ellipse3 = patches.Ellipse((0.5, 0.2), width=0.4, height=0.2, facecolor='green', alpha=1)
ax.add_patch(ellipse3)

# Додавання контурів
for e in [ellipse1, ellipse2, ellipse3]:
    ellipse_contour = patches.Ellipse(xy=e.center, width=e.width, height=e.height, fill=False, edgecolor='black',
                                      linewidth=1, alpha=1.0)
    ax.add_patch(ellipse_contour)

# Налаштування відображення
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')

def init():
    return ellipse1, ellipse2, ellipse3 

iterations = 0
# Ініціалізація анімації
def update(frame):
    global iterations
    if frame < 10:
        ellipse1.set_alpha(0.1 * frame)
        ellipse3.set_alpha(1 - 0.11 * frame)
    elif frame < 20:
        ellipse3.set_alpha(0)
        ellipse1.set_alpha(1 - 0.1 * (frame - 10))
        ellipse3.set_alpha(0.11 * (frame - 10))
    elif frame < 25:
        ellipse1.set_alpha(0)
        ellipse3.set_alpha(1 - 0.14 * (frame - 20))
    else:
        ellipse3.set_alpha(0)

        # Changing color of ellipse2 for 2 frames
        if frame % 5 == 0 and frame < 35:
            ellipse2.set_alpha(1)
            ellipse2.set_facecolor('yellow')
        else:
            ellipse2.set_facecolor('white')
    
    iterations += 1
    if iterations == 400: #400 кадрів ( тобто 10 разів по 40)
       ani.event_source.stop()

ani = FuncAnimation(fig, update, init_func=init, frames=40, repeat=10)
ani.save('sf.gif', writer='pillow', fps=40)
plt.show()
