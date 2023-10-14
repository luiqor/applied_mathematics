import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define the coordinates of the dodecagon vertices
center = [1, 0]  # Center of the dodecagon
radius = 1       # Radius of the dodecagon

num_vertices = 12
angle = np.linspace(0, 2 * np.pi, num_vertices, endpoint=False)
x = center[0] + radius * np.cos(angle)
y = center[1] + radius * np.sin(angle)

# Create a new figure and axis
fig, ax = plt.subplots()

# Create a dodecagon patch with the defined vertices
dodecagon = patches.Polygon(np.column_stack((x, y)), closed=True, facecolor='orange', edgecolor='black')

# Add the dodecagon patch to the axis
ax.add_patch(dodecagon)

# Add text in the middle of the dodecagon
ax.text(center[0], center[1], '12-кутник', ha='center', va='center', color = 'w', fontweight='bold')

# Add arrows to the edges of the dodecagon using FancyArrowPatch
for i in range(len(x)):
    dx, dy = x[(i + 1) % len(x)] - x[i], y[(i + 1) % len(y)] - y[i]
    arrow = patches.FancyArrowPatch((x[i], y[i]), (x[i] + dx, y[i] + dy), color='purple', arrowstyle='->', mutation_scale=15, linewidth=3.0)
    ax.add_patch(arrow)

# Set the axis limits and aspect ratio
ax.set_xlim(-1.5, 3.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Display the plot
plt.show()

#GOOD
