import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
center = [1, 0]  # Центр 12кутника
radius = 1       # Радіус 12кутника

num_vertices = 12
angle = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
x = center[0] + radius * np.cos(angle)
y = center[1] + radius * np.sin(angle)

fig, ax = plt.subplots()
dodecagon = patches.Polygon(np.column_stack((x, y)), closed=True, facecolor='orange', edgecolor='black')
ax.add_patch(dodecagon)

ax.text(center[0], center[1], '12-кутник', ha='center', va='center', color = 'w', fontweight='bold')

for i in range(len(x)):
    dx, dy = x[(i + 1) % len(x)] - x[i], y[(i + 1) % len(y)] - y[i]
    arrow = patches.FancyArrowPatch((x[i], y[i]), (x[i] + dx, y[i] + dy), color='purple', arrowstyle='->', mutation_scale=15, linewidth=3.0)
    ax.add_patch(arrow)

ax.set_xlim(-1.5, 3.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

plt.show()

#GOOD
