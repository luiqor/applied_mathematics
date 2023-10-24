import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def polar_curve(phi):
        r = 3 * np.sin(5 * phi)
        return r, phi

frames = 360
duration = 10

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}) 
line, = ax.plot([], [], lw=2)
ax.set_rmax(3)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    if frame < frames:
            phi = np.linspace(0, 2 * np.pi, frames)
            r, phi = polar_curve(phi)
            line.set_data(phi[:frame], r[:frame])
    else:
            rotation_degree = (frame - frames) * 2
            ax.set_rlabel_position(rotation_degree * np.pi / 180)
            ax.set_theta_offset(rotation_degree * np.pi / 180)
    return line,

ani = animation.FuncAnimation(fig, update, init_func=init, frames = frames + 180, blit=True, interval = duration / (frames +180) * 1000)
plt.show()
# # Add the third subplot with a polar plot
# ax3 = fig.add_axes([left3, bottom3, width3, height3], projection='polar')
# fi = np.linspace(-np.pi, np.pi, 5000)
# r = np.abs(3 * np.sin(2 * fi))
# ax3.plot(fi, r, color='purple')
# ax3.fill(fi, r, color='yellow')
# ax3.set_title('Полярний графік')
# plt.tight_layout()