import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create the figure with a subplot for the polar plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# Create the initial data for the polar plot
theta = np.linspace(0, 2 * np.pi, 1000)
r = np.abs(3 * np.sin(4 * theta))

line, = ax.plot(theta, r, color='purple')
ax.set_title('Полярний графік')

# Initialize a function to update the polar plot
def init():
    line.set_ydata(np.ma.array(theta))
    return line,

def update(frame):
    # Modify the parameters for the 4-petal rose
    theta = np.linspace(0, 2 * np.pi, 1000)
    r = np.abs(3 * np.sin(2 * theta + 0.1 * frame))
    line.set_ydata(r)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, init_func=init, frames=range(1, 500), blit=True, interval=20)

plt.tight_layout()
plt.show()



# # Add the third subplot with a polar plot
# ax3 = fig.add_axes([left3, bottom3, width3, height3], projection='polar')
# fi = np.linspace(-np.pi, np.pi, 5000)
# r = np.abs(3 * np.sin(2 * fi))
# ax3.plot(fi, r, color='purple')
# ax3.fill(fi, r, color='yellow')
# ax3.set_title('Полярний графік')
# plt.tight_layout()