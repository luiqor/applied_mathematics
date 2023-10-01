import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 400)
y1 = np.linspace(-3, 3, 400)

X, Y1 = np.meshgrid(x, y1)
equation = X**2 / 20 + Y1**2 / 5 - 1

y2 = (6-12*x)/5

plt.figure(figsize=(9, 9))
plt.title("Залежності: ") 
plt.xlabel("x") 
plt.ylabel("y1, y2")
plt.grid()
plt.plot(x, y2, color = "g", linestyle='--', lw=3)
plt.contour(X,Y1,equation, levels=[0], colors="magenta", linestyles = "-.", linewidths = 1)
# oval=... + oval.collections[0].set_label('X**2 / 20 + Y**2 / 5 - 1 = 1')

custom_legend_plot = [plt.Line2D([0], [0], color='g',linestyle='--', lw=3, label='y2 = (6-12*x)/5')]
custom_legend_contour = [plt.Line2D([0], [0], color='magenta',linestyle="-.", lw=1, label='X**2 / 20 + Y**2 / 5 - 1 = 1')]
plt.legend(handles=custom_legend_contour + custom_legend_plot)

plt.grid(True)
plt.show()