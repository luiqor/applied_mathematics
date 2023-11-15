import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the figure with a subplot for the polar plot
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
frames = 500

line, = ax.plot([], [], lw=2)
ax.set_rmax(4)

def init():
    line.set_data([], [])
    return line,

def update(frames):
        theta = np.linspace(0, 2 * np.pi, frames)
        r = np.abs(3 * np.sin(2 * theta + 0.05 * frames))
        line.set_data(theta, r)
        return line,
   

# Create the animation  
ani = animation.FuncAnimation(fig, update, init_func=init, 
                              frames=frames, blit=True, repeat = False, interval = 24)

ax.set_title('Полярний графік')
plt.show()


# # Add the third subplot with a polar plot
# ax3 = fig.add_axes([left3, bottom3, width3, height3], projection='polar')
# fi = np.linspace(-np.pi, np.pi, 5000)
# r = np.abs(3 * np.sin(2 * fi))
# ax3.plot(fi, r, color='purple')
# ax3.fill(fi, r, color='yellow')
# ax3.set_title('Полярний графік')
# plt.tight_layout()