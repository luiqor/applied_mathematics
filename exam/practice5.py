import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Choose a phi != pi/2
phi = np.pi/3  

# Parametric equations for the circle
theta = np.linspace(0, 2*np.pi, 100)
phi = phi * np.ones_like(theta)

xs = np.cos(theta) * np.sin(phi) 
ys = np.sin(theta) * np.sin(phi)
zs = np.cos(phi)

# Plot sphere and circle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, color='magenta', alpha=0.15)
#Коло
ax.plot(zs, xs, ys, c='red')

ax.set_xlim(-1,1)
ax.set_ylim(-1,1) 
ax.set_zlim(-1,1)
ax.set_box_aspect([2, 2, 2])

plt.show()